import time
import random
import pandas as pd
from bot.notifier import send_sell_alert
import yaml

# Load settings
with open("config/settings.yaml") as f:
    settings = yaml.safe_load(f)

PAIR = settings['weltrade']['pair']
TIMEFRAMES = ["1m", "5m", "15m"]

def fetch_dummy_data():
    """Simulated OHLC data for testing without MT5"""
    data = {
        "open": [random.uniform(100, 110) for _ in range(200)],
        "close": [random.uniform(100, 110) for _ in range(200)],
        "high": [random.uniform(110, 115) for _ in range(200)],
        "low": [random.uniform(95, 100) for _ in range(200)],
    }
    return pd.DataFrame(data)

def check_for_sell_signal(df, timeframe):
    """Check if last candle is bullish (buy) and send SELL alert"""
    last = df.iloc[-1]
    if last['close'] > last['open']:
        entry = last['close']
        tp = last['low']
        send_sell_alert(PAIR, entry, tp, timeframe)

def main():
    while True:
        for tf in TIMEFRAMES:
            df = fetch_dummy_data()
            check_for_sell_signal(df, tf)
        time.sleep(60)  # run every minute

if __name__ == "__main__":
    main()
