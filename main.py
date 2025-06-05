from bot.api import get_exchange, get_balance
from bot.strategy import rsi_strategy
from bot.backtest import simulate
from bot.notify import send_discord
import pandas as pd
import os

# mock historical data
df = pd.read_csv("sample_data.csv")
df = rsi_strategy(df)
trades, count = simulate(df)

# Notify result
send_discord(f"Simulated {count} trades. Last trade price: {trades[-1] if trades else 'N/A'}")

# Run real balance check
exchange = get_exchange()
balance = get_balance(exchange)
print("Your balance:", balance['total'])
