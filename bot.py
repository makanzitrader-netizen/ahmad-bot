import requests

TELEGRAM_TOKEN = "8592300292:AAErZvhkkIwaHhAVzzJYIgfg0LLPpf9s3hA"
CHAT_ID = "7561205372"
OPENROUTER_API = "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"

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
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://ahmad-bot.onrender.com",
            "X-Title": "Ahmad Intelligence Bot"
        },
        json={
            "model": "moonshotai/kimi-k2:free",
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
        message = f"Unexpected response: {str(data)}"

except Exception as e:
    message = f"Bot error: {str(e)}"

requests.post(
    f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
    json={"chat_id": CHAT_ID, "text": message}
)
