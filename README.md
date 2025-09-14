# Weltrade GainX 800 Sell-After-Buy-Candle Bot

This bot monitors GainX 800 on Weltrade demo and executes **SELL trades** immediately after a **buy candle closes** on 1M, 5M, and 15M timeframes. TP is set to the **low of the candle that triggered the sell**.  

## Setup
1. Install Python 3.11+
2. Install dependencies: `pip install -r requirements.txt`
3. Update `config/settings.yaml` with your Weltrade demo login
4. Run: `python main.py`
