import requests
import yaml

with open("config/settings.yaml") as f:
    settings = yaml.safe_load(f)

BOT_TOKEN = settings['telegram']['token']
CHAT_ID = settings['telegram']['chat_id']

def send_trade_alert(pair, direction, timeframe, entry, sl, tp1, tp2, tp3):
    message = (
        f"📊 Trade Alert\n\n"
        f"Pair: {pair}\n"
        f"Timeframe: {timeframe}\n"
        f"Direction: {direction}\n"
        f"Entry: {entry}\n"
        f"SL: {sl}\n"
        f"TP1: {tp1}\n"
        f"TP2: {tp2}\n"
        f"TP3: {tp3}"
    )
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": message})
