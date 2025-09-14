import pandas as pd

def detect_swing_high_low(df, window=5):
    highs = df['high']
    lows = df['low']
    swing_highs = [i for i in range(window, len(highs)-window) if highs[i] == max(highs[i-window:i+window])]
    swing_lows = [i for i in range(window, len(lows)-window) if lows[i] == min(lows[i-window:i+window])]
    return swing_highs, swing_lows

def detect_choch_bos(df):
    swing_highs, swing_lows = detect_swing_high_low(df)
    last_close = df['close'].iloc[-1]

    direction = None
    if len(swing_highs) >= 2 and last_close > df['high'].iloc[swing_highs[-2]]:
        direction = "buy"
    elif len(swing_lows) >= 2 and last_close < df['low'].iloc[swing_lows[-2]]:
        direction = "sell"
    return direction
