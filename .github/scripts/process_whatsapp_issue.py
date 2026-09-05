#!/usr/bin/env python3
"""
AI Agent to transform raw WhatsApp messages into formatted GitHub Issues.
Supports Google Gemini (default, free API) or OpenAI.
"""

import json
import os
import sys
import subprocess
import urllib.request
import urllib.error


def call_gemini(prompt: str, api_key: str) -> dict:
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "response_mime_type": "application/json",
            "temperature": 0.2,
        },
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req) as resp:
        result = json.loads(resp.read().decode("utf-8"))
        text = result["candidates"][0]["content"]["parts"][0]["text"]
        return json.loads(text)


def call_openai(prompt: str, api_key: str) -> dict:
    url = "https://api.openai.com/v1/chat/completions"
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "system",
                "content": "You convert informal messages into structured GitHub issues. Output only valid JSON.",
            },
            {"role": "user", "content": prompt},
        ],
        "response_format": {"type": "json_object"},
        "temperature": 0.2,
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
    )
    with urllib.request.urlopen(req) as resp:
        result = json.loads(resp.read().decode("utf-8"))
        text = result["choices"][0]["message"]["content"]
        return json.loads(text)


def send_whatsapp_reply(phone_number_id: str, access_token: str, to: str, message: str):
    """Optionally send a confirmation message back to WhatsApp."""
    if not (phone_number_id and access_token and to):
        return
    url = f"https://graph.facebook.com/v20.0/{phone_number_id}/messages"
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": message},
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}",
        },
    )
    try:
        with urllib.request.urlopen(req) as resp:
            print(f"WhatsApp reply sent successfully: {resp.status}")
    except Exception as e:
        print(f"Failed to send WhatsApp reply: {e}")


def main():
    raw_message = os.environ.get("WHATSAPP_MESSAGE", "").strip()
    sender = os.environ.get("WHATSAPP_SENDER", "WhatsApp User")
    gemini_key = os.environ.get("GEMINI_API_KEY")
    openai_key = os.environ.get("OPENAI_API_KEY")
    repo = os.environ.get("GITHUB_REPOSITORY", "kavix/kavix")

    if not raw_message:
        print("Error: WHATSAPP_MESSAGE is empty.")
        sys.exit(1)

    ai_prompt = f"""
You are an expert GitHub issue triage AI assistant.
Convert this raw message received from WhatsApp into a well-structured GitHub issue for repository `{repo}`.

Raw WhatsApp Message:
\"\"\"{raw_message}\"\"\"
Sender: {sender}

Respond ONLY with valid JSON matching this schema:
{{
  "title": "Clear, descriptive title summarizing the issue",
  "body": "Formatted GitHub markdown description including Summary, Details, WhatsApp metadata (sender), and Next Steps",
  "labels": ["whatsapp"]
}}
"""

    print("Analyzing message with AI...")
    parsed_issue = None

    if gemini_key:
        print("Using Google Gemini...")
        parsed_issue = call_gemini(ai_prompt, gemini_key)
    elif openai_key:
        print("Using OpenAI...")
        parsed_issue = call_openai(ai_prompt, openai_key)
    else:
        print("No AI key provided. Falling back to default formatting.")
        parsed_issue = {
            "title": f"[WhatsApp] {raw_message[:60]}...",
            "body": f"### WhatsApp Message\n\n{raw_message}\n\n**Sender:** `{sender}`",
            "labels": ["whatsapp"],
        }

    title = parsed_issue.get("title", f"[WhatsApp] {raw_message[:50]}")
    body = parsed_issue.get("body", raw_message)
    labels = parsed_issue.get("labels", ["whatsapp"])

    # Create the issue using GitHub CLI
    cmd = [
        "gh",
        "issue",
        "create",
        "--repo",
        repo,
        "--title",
        title,
        "--body",
        body,
    ]
    for label in labels:
        cmd.extend(["--label", label.strip()])

    print(f"Creating GitHub issue: {title}")
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        # If label doesn't exist, retry without labels
        print(f"Issue creation with labels encountered: {result.stderr}. Retrying without labels...")
        cmd_fallback = [
            "gh",
            "issue",
            "create",
            "--repo",
            repo,
            "--title",
            title,
            "--body",
            body,
        ]
        result = subprocess.run(cmd_fallback, capture_output=True, text=True, check=True)

    issue_url = result.stdout.strip()
    print(f"Successfully created issue: {issue_url}")

    # Optional: Send WhatsApp notification back
    phone_id = os.environ.get("WHATSAPP_PHONE_NUMBER_ID")
    wa_token = os.environ.get("WHATSAPP_ACCESS_TOKEN")
    if phone_id and wa_token and sender and sender.isdigit():
        reply_msg = f" Issue created in {repo}:\n{issue_url}\n\nTitle: {title}"
        send_whatsapp_reply(phone_id, wa_token, sender, reply_msg)


if __name__ == "__main__":
    main()
