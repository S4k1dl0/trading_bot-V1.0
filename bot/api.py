import ccxt
import os

def get_exchange():
    return ccxt.binance({
        'apiKey': os.getenv("BINANCE_API_KEY"),
        'secret': os.getenv("BINANCE_API_SECRET"),
        'enableRateLimit': True
    })

def get_balance(exchange):
    return exchange.fetch_balance()
