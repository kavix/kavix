/**
 * Cloudflare Worker: WhatsApp Cloud API to GitHub Action Relay
 * 
 * Environment Variables required in Cloudflare Worker dashboard:
 * - WHATSAPP_VERIFY_TOKEN: Any secret string you choose for webhook verification
 * - GITHUB_PAT: GitHub Personal Access Token (classic with repo scope, or fine-grained with Actions:write)
 * - GITHUB_REPO: "kavix/kavix"
 * - ALLOWED_PHONES: (Optional) Comma-separated list of allowed phone numbers (e.g. "1234567890,9876543210")
 */

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    // 1. WhatsApp Webhook Verification (GET request)
    if (request.method === "GET") {
      const mode = url.searchParams.get("hub.mode");
      const token = url.searchParams.get("hub.verify_token");
      const challenge = url.searchParams.get("hub.challenge");

      if (mode === "subscribe" && token === env.WHATSAPP_VERIFY_TOKEN) {
        return new Response(challenge, { status: 200 });
      }
      return new Response("Forbidden", { status: 403 });
    }

    // 2. Incoming WhatsApp Message (POST request)
    if (request.method === "POST") {
      try {
        const body = await request.json();

        // Extract message details from WhatsApp Cloud API payload
        const entry = body.entry?.[0];
        const change = entry?.changes?.[0];
        const value = change?.value;
        const message = value?.messages?.[0];

        if (!message || message.type !== "text") {
          return new Response("Not a text message or status update", { status: 200 });
        }

        const sender = message.from; // e.g. "94771234567"
        const messageText = message.text?.body;

        // Security check: Only allow your authorized phone number(s)
        if (env.ALLOWED_PHONES) {
          const allowed = env.ALLOWED_PHONES.split(",").map(p => p.trim());
          if (!allowed.includes(sender)) {
            console.log(`Ignored message from unauthorized sender: ${sender}`);
            return new Response("Unauthorized sender", { status: 200 });
          }
        }

        // Trigger GitHub Action repository_dispatch
        const ghRepo = env.GITHUB_REPO || "kavix/kavix";
        const ghResponse = await fetch(`https://api.github.com/repos/${ghRepo}/dispatches`, {
          method: "POST",
          headers: {
            "Authorization": `Bearer ${env.GITHUB_PAT}`,
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "WhatsApp-GitHub-Relay",
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            event_type: "whatsapp_issue",
            client_payload: {
              sender: sender,
              message: messageText
            }
          })
        });

        if (!ghResponse.ok) {
          const errText = await ghResponse.text();
          console.error(`GitHub dispatch failed: ${ghResponse.status} ${errText}`);
          return new Response("GitHub dispatch error", { status: 500 });
        }

        return new Response("Dispatched to GitHub Action", { status: 200 });
      } catch (err) {
        console.error("Error processing webhook:", err);
        return new Response("Internal Server Error", { status: 500 });
      }
    }

    return new Response("Method not allowed", { status: 405 });
  }
};
