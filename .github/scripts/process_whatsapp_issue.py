#!/usr/bin/env python3
"""
AI Agent to transform raw WhatsApp messages into formatted GitHub Issues.
Supports Google Gemini, OpenAI, and fallback to direct issue creation.
"""

import json
import os
import sys
import subprocess
import urllib.request
import urllib.parse
import urllib.error


def call_gemini(prompt: str, api_key: str) -> dict:
    models = ["gemini-2.5-flash", "gemini-2.0-flash", "gemini-1.5-flash-latest", "gemini-1.5-flash"]
    last_error = None
    for model in models:
        for version in ["v1beta", "v1"]:
            url = f"https://generativelanguage.googleapis.com/{version}/models/{model}:generateContent?key={api_key}"
            payload = {
                "contents": [{"parts": [{"text": prompt}]}],
                "generationConfig": {
                    "response_mime_type": "application/json",
                    "temperature": 0.2,
                },
            }
            try:
                req = urllib.request.Request(
                    url,
                    data=json.dumps(payload).encode("utf-8"),
                    headers={"Content-Type": "application/json"},
                )
                with urllib.request.urlopen(req) as resp:
                    result = json.loads(resp.read().decode("utf-8"))
                    text = result["candidates"][0]["content"]["parts"][0]["text"]
                    return json.loads(text)
            except Exception as e:
                last_error = e
                continue
    raise RuntimeError(f"All Gemini models failed. Last error: {last_error}")


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
    """Send confirmation message back via Meta WhatsApp Cloud API."""
    if not (phone_number_id and access_token and to):
        return
    clean_to = to.lstrip("+").strip()
    url = f"https://graph.facebook.com/v20.0/{phone_number_id}/messages"
    payload = {
        "messaging_product": "whatsapp",
        "to": clean_to,
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
            print(f"WhatsApp Cloud API reply sent: {resp.status}")
    except urllib.error.HTTPError as e:
        error_details = e.read().decode("utf-8")
        print(f"Failed to send WhatsApp Cloud API reply: HTTP {e.code}: {error_details}")
    except Exception as e:
        print(f"Failed to send WhatsApp Cloud API reply: {e}")


def send_callmebot_reply(phone: str, apikey: str, message: str):
    """Send confirmation message back via CallMeBot."""
    if not (phone and apikey):
        return
    clean_phone = phone.lstrip("+").strip()
    encoded = urllib.parse.quote(message)
    url = f"https://api.callmebot.com/whatsapp.php?phone={clean_phone}&text={encoded}&apikey={apikey}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "GitHub-Action"})
        with urllib.request.urlopen(req) as resp:
            print(f"CallMeBot reply sent: {resp.status}")
    except Exception as e:
        print(f"CallMeBot reply failed: {e}")


def main():
    raw_message = os.environ.get("WHATSAPP_MESSAGE", "").strip()
    sender = os.environ.get("WHATSAPP_SENDER", "WhatsApp User")
    gemini_key = os.environ.get("GEMINI_API_KEY")
    openai_key = os.environ.get("OPENAI_API_KEY")
    callmebot_key = os.environ.get("CALLMEBOT_API_KEY")
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

    parsed_issue = None

    if gemini_key:
        print("Attempting AI parsing with Google Gemini...")
        try:
            parsed_issue = call_gemini(ai_prompt, gemini_key)
        except Exception as e:
            print(f"Gemini error: {e}. Falling back to default format.")

    if not parsed_issue and openai_key:
        print("Attempting AI parsing with OpenAI...")
        try:
            parsed_issue = call_openai(ai_prompt, openai_key)
        except Exception as e:
            print(f"OpenAI error: {e}. Falling back to default format.")

    if not parsed_issue:
        print("Using fallback issue formatting.")
        parsed_issue = {
            "title": f"[WhatsApp] {raw_message[:60]}",
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
        print(f"Creating without labels due to: {result.stderr}")
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

    # Send WhatsApp notification back
    reply_msg = f" Issue created in {repo}:\n{issue_url}\n\nTitle: {title}"

    phone_id = os.environ.get("WHATSAPP_PHONE_NUMBER_ID")
    wa_token = os.environ.get("WHATSAPP_ACCESS_TOKEN")
    if phone_id and wa_token and sender:
        send_whatsapp_reply(phone_id, wa_token, sender, reply_msg)

    if callmebot_key and sender:
        send_callmebot_reply(sender, callmebot_key, reply_msg)


if __name__ == "__main__":
    main()
