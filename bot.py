import requests

TELEGRAM_TOKEN = "8592300292:AAFV6LicNEJl03QX-F7X_ZKO2C7dCEloT8M"
CHAT_ID = "7561205372"
KIMI_API = "sk-IneUi2Wsb7Mpdym1xVaibbrtZstAQwkLquQBQx5wapDytG50"

prompt = """You are Ahmad's personal intelligence agent based in Dubai. Deliver today's briefing:

🔴 WAR & REGION
- Latest Iran-US-UAE development in last 24 hours
- Threat level: HIGHER / SAME / LOWER vs yesterday

🏗️ UAE & GCC
- Real estate market move today (Emaar, Aldar, off-plan)
- Construction or financing news in GCC

📈 MARKETS & HALAL
- Gold price today and direction
- Best halal opportunity or risk right now

🤖 AI EDGE
- One AI tool worth knowing this week

💡 AHMAD'S EDGE
- One insight most people are missing today

⚡ TODAY'S ACTION
- One specific thing Ahmad should do today

Be direct. No filler. Max 2 lines per bullet."""

try:
    response = requests.post(
        "https://api.moonshot.ai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {KIMI_API}",
            "Content-Type": "application/json"
        },
        json={
            "model": "moonshot-v1-8k",
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 1000
        }
    )

    data = response.json()

    if "choices" in data:
        message = data["choices"][0]["message"]["content"]
    elif "error" in data:
        message = f"API Error: {data['error']}"
    else:
        message = f"Unexpected: {str(data)}"

except Exception as e:
    message = f"Error: {str(e)}"

requests.post(
    f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
    json={"chat_id": CHAT_ID, "text": message}
)
