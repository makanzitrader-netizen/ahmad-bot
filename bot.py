import requests

TELEGRAM_TOKEN = "8592300292:AAErZvhkkIwaHhAVzzJYIgfg0LLPpf9s3hA"
CHAT_ID = "7561205372"
KIMI_API = "sk-F9gqH4gjNwO6ibKE7mXNURxZXnf5bP7MUQfmptXqUAtR7iKv"

prompt = """You are Ahmad's personal intelligence agent based in Dubai. Search the web for today's latest news and deliver this briefing:

🔴 WAR & REGION
- Latest Iran-US-UAE development in last 24 hours
- Threat level change vs yesterday: HIGHER / SAME / LOWER

🏗️ UAE & GCC
- Real estate market move today (Emaar, Aldar, off-plan)
- Construction or financing news in GCC

📈 MARKETS & HALAL
- Gold price today and direction
- Best halal opportunity or risk right now

🤖 AI EDGE
- One AI tool or development worth acting on this week

💡 AHMAD'S EDGE
- One non-obvious insight most people are missing today

⚡ TODAY'S ACTION
- One specific thing Ahmad should do today

Keep every bullet under 2 lines. Be direct. No filler."""

response = requests.post(
    "https://api.moonshot.cn/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {KIMI_API}",
        "Content-Type": "application/json"
    },
    json={
        "model": "moonshot-v1-8k",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 1000
    }
).json()

message = response["choices"][0]["message"]["content"]

requests.post(
    f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
    json={"chat_id": CHAT_ID, "text": message}
)
