import time
from strategy.live_data_mt5 import connect_to_broker, get_ohlc
from strategy.simple_entry import detect_buy_candle_close
from strategy.mt5_orders import place_order
import MetaTrader5 as mt5

symbol = "GainX 800"
TIMEFRAMES = [mt5.TIMEFRAME_M1, mt5.TIMEFRAME_M5, mt5.TIMEFRAME_M15]
lot_size = 0.1

broker_config = {
    "login": 19445845,
    "password": "kR7(5Gw(",
    "server": "Weltrade-Demo"
}

if connect_to_broker("weltrade_demo", broker_config):
    while True:
        for tf in TIMEFRAMES:
            df = get_ohlc(symbol, timeframe=tf, num_bars=200)
            if df is not None:
                is_buy_candle, tp_price = detect_buy_candle_close(df)
                if is_buy_candle:
                    entry_price = df[-1]['close']
                    sl = df[-1]['high']
                    place_order(symbol, lot=lot_size, entry=entry_price, sl=sl, tp=tp_price, order_type="SELL")
        time.sleep(30)
