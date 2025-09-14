import requests
import yaml

with open("config/settings.yaml") as f:
    settings = yaml.safe_load(f)

BOT_TOKEN = settings['telegram']['token']
CHAT_ID = settings['telegram']['chat_id']

def send_sell_alert(pair, entry, tp, timeframe):
    message = (
        f"📊 SELL Signal (Weltrade Demo)\n\n"
        f"Pair: {pair}\n"
        f"Entry: {entry}\n"
        f"TP: {tp}\n"
        f"Timeframe: {timeframe}\n"
        f"Condition: Buy candle closed → SELL"
    )

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    response = requests.post(url, data={"chat_id": CHAT_ID, "text": message})

    if response.status_code != 200:
        print("⚠️ Failed to send alert:", response.text)
