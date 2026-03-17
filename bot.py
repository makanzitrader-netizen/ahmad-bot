import requests

TELEGRAM_TOKEN = "8592300292:AAErZvhkkIwaHhAVzzJYIgfg0LLPpf9s3hA"
CHAT_ID = "7561205372"
GEMINI_API = "AIzaSyDCxnsldCR8YXjZVUj5YwqWDqgsTYbpaXA"

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
        f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API}",
        headers={"Content-Type": "application/json"},
        json={
            "contents": [{"parts": [{"text": prompt}]}]
        }
    )

    data = response.json()

    if "candidates" in data:
        message = data["candidates"][0]["content"]["parts"][0]["text"]
    elif "error" in data:
        message = f"API Error: {data['error']['message']}"
    else:
        message = f"Unexpected response: {str(data)}"

except Exception as e:
    message = f"Bot error: {str(e)}"

requests.post(
    f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
    json={"chat_id": CHAT_ID, "text": message}
)
