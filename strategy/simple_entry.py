def detect_buy_candle_close(df):
    """
    Returns True if the last candle closed bullish (buy candle)
    Also returns the low of that candle for TP
    """
    last_candle = df[-1]  # df can be a list of dicts or DataFrame rows
    if last_candle['close'] > last_candle['open']:
        return True, last_candle['low']
    return False, None
