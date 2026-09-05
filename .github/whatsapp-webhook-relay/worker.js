export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    // 1. WhatsApp Webhook Verification (GET request)
    if (request.method === "GET") {
      const mode = url.searchParams.get("hub.mode");
      const token = url.searchParams.get("hub.verify_token");
      const challenge = url.searchParams.get("hub.challenge");

      const expectedToken = (env.WHATSAPP_VERIFY_TOKEN || "kavix_secret_123").trim();

      if (mode === "subscribe" && token === expectedToken) {
        return new Response(challenge, {
          status: 200,
          headers: { "Content-Type": "text/plain" }
        });
      }
      return new Response(`Forbidden: received token '${token}'`, { status: 403 });
    }

    // 2. Incoming WhatsApp Message (POST request)
    if (request.method === "POST") {
      try {
        const body = await request.json();

        const entry = body.entry?.[0];
        const change = entry?.changes?.[0];
        const value = change?.value;
        const message = value?.messages?.[0];

        if (!message || message.type !== "text") {
          return new Response("Not a text message or status update", { status: 200 });
        }

        const sender = message.from;
        const messageText = message.text?.body;

        // Security check: match phone number flexibly (handles +, spaces, country code)
        if (env.ALLOWED_PHONES && env.ALLOWED_PHONES.trim() !== "") {
          const cleanSender = String(sender).replace(/\D/g, "");
          const allowedList = env.ALLOWED_PHONES.split(",")
            .map(p => p.replace(/\D/g, "").trim())
            .filter(Boolean);

          const isAllowed = allowedList.some(p => cleanSender.endsWith(p) || p.endsWith(cleanSender));
          if (!isAllowed) {
            console.log(`Blocked unauthorized sender: ${sender}`);
            return new Response(`Unauthorized sender: ${sender}`, { status: 200 });
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
          return new Response(`GitHub dispatch error: ${ghResponse.status} ${errText}`, { status: 500 });
        }

        return new Response("Dispatched to GitHub Action", { status: 200 });
      } catch (err) {
        console.error("Error processing webhook:", err);
        return new Response(`Internal Server Error: ${err.message}`, { status: 500 });
      }
    }

    return new Response("Method not allowed", { status: 405 });
  }
};
