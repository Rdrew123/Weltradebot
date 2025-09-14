import MetaTrader5 as mt5

def connect_to_broker(name, config):
    if not mt5.initialize(server=config["server"], login=config["login"], password=config["password"]):
        print(f"⚠️ Failed to connect: {mt5.last_error()}")
        return False
    print(f"✅ Connected to {name}")
    return True

def get_ohlc(symbol, timeframe=mt5.TIMEFRAME_M1, num_bars=200):
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, num_bars)
    return rates
