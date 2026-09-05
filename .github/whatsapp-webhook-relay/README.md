# WhatsApp to GitHub Issue Relay Setup

This directory contains the free serverless bridge connecting WhatsApp to GitHub Actions.

## Setup Steps

### 1. WhatsApp Cloud API Setup (Meta for Developers)
1. Go to [developers.facebook.com](https://developers.facebook.com/) and create a Meta App (Type: **Business**).
2. Add **WhatsApp** product to your app.
3. In the WhatsApp API Setup page, you will get:
   - A test WhatsApp phone number and test recipient phone.
   - **Phone Number ID** (for sending replies back).
   - **Temporary Access Token** (or create a permanent System User token in Business Settings).

### 2. Deploy the Cloudflare Worker (Free Relay)
1. Go to [dash.cloudflare.com](https://dash.cloudflare.com/) > **Workers & Pages** > **Create application** > **Worker**.
2. Paste the contents of [`worker.js`](worker.js).
3. Under **Settings > Variables**, configure:
   - `WHATSAPP_VERIFY_TOKEN`: Any secret password you pick (e.g. `my_super_secret_token_123`).
   - `GITHUB_PAT`: A GitHub Personal Access Token (with `repo` permissions to trigger `repository_dispatch`).
   - `GITHUB_REPO`: `kavix/kavix`.
   - `ALLOWED_PHONES`: Your phone number with country code (e.g. `94771234567`) to prevent unauthorized triggers.
4. Deploy the worker and copy its URL (e.g., `https://whatsapp-relay.your-subdomain.workers.dev`).

### 3. Link Worker to WhatsApp
1. In Meta Developer Portal > WhatsApp > **Configuration**:
   - **Callback URL**: `https://whatsapp-relay.your-subdomain.workers.dev`
   - **Verify Token**: The same value you set for `WHATSAPP_VERIFY_TOKEN`.
2. Click **Verify and Save**.
3. Under **Webhook fields**, subscribe to `messages`.

### 4. Configure GitHub Repository Secrets
In `kavix/kavix` > **Settings** > **Secrets and variables** > **Actions**, add:
- `GEMINI_API_KEY`: Free key from [Google AI Studio](https://aistudio.google.com/) (or `OPENAI_API_KEY`).
- *(Optional)* `WHATSAPP_ACCESS_TOKEN`: WhatsApp Cloud API token (if you want the agent to reply on WhatsApp with the issue link).
- *(Optional)* `WHATSAPP_PHONE_NUMBER_ID`: WhatsApp Phone Number ID.
