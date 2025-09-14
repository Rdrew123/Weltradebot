import MetaTrader5 as mt5

def place_order(symbol, lot, entry, sl, tp, order_type="SELL"):
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": mt5.ORDER_TYPE_SELL,
        "price": entry,
        "sl": sl,
        "tp": tp,
        "deviation": 10,
        "magic": 234002,
        "comment": "GainX800 SellBot",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_RETURN,
    }
    result = mt5.order_send(request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print(f"⚠️ Failed SELL order:", result)
    else:
        print(f"✅ SELL order placed at {entry} with TP {tp}")
