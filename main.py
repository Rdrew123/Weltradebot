import time
import pandas as pd
import requests
from bot.notifier import send_trade_alert
from strategy.structure import detect_choch_bos
import yaml

with open("config/settings.yaml") as f:
    settings = yaml.safe_load(f)

FMP_KEY = settings['api']['fmp_key']
PAIR = settings['pair']['symbol']

price_history_m1 = []
price_history_m5 = []

def fetch_usdjpy():
    url = f"https://financialmodelingprep.com/api/v3/quote/{PAIR}?apikey={FMP_KEY}"
    response = requests.get(url).json()
    return response[0]['price']

def simulate_candle(price_list):
    df = pd.DataFrame(price_list, columns=['close'])
    df['high'] = df['close']
    df['low'] = df['close']
    return df

def run_bot():
    while True:
        price = fetch_usdjpy()
        price_history_m1.append(price)
        if len(price_history_m1) > 5:
            df_m1 = simulate_candle(price_history_m1[-5:])
            direction = detect_choch_bos(df_m1)
            if direction:
                send_trade_alert(
                    PAIR,
                    direction,
                    "M1",
                    price,
                    price-0.1 if direction=="buy" else price+0.1,
                    price+0.1 if direction=="buy" else price-0.1,
                    price+0.2 if direction=="buy" else price-0.2,
                    price+0.3 if direction=="buy" else price-0.3
                )

        price_history_m5.append(price)
        if len(price_history_m5) >= 5:
            df_m5 = simulate_candle(price_history_m5[-5:])
            direction = detect_choch_bos(df_m5)
            if direction:
                send_trade_alert(
                    PAIR,
                    direction,
                    "M5",
                    price,
                    price-0.1 if direction=="buy" else price+0.1,
                    price+0.1 if direction=="buy" else price-0.1,
                    price+0.2 if direction=="buy" else price-0.2,
                    price+0.3 if direction=="buy" else price-0.3
                )
            price_history_m5.clear()

        time.sleep(60)

if __name__ == "__main__":
    run_bot()
