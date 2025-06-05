from flask import Flask, request, jsonify, session
from flask_cors import CORS
import pandas as pd
from bot.strategy import rsi_strategy, dca_strategy, grid_strategy, macd_strategy
from bot.backtest import simulate
from bot.ml_model import train_model
from db import init_db, log_message
import sqlite3
from auth import auth

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.secret_key = "supersecret"
app.register_blueprint(auth)

init_db()

@app.route("/summary", methods=["GET"])
def summary():
    df = pd.read_csv("sample_data.csv")
    df = rsi_strategy(df)
    trades, count = simulate(df)
    return jsonify({
        "trades_count": count,
        "last_trade_price": trades[-1] if trades else None
    })

@app.route("/strategy", methods=["POST"])
def run_strategy():
    data = request.json
    df = pd.read_csv("sample_data.csv")
    strategy_used = []

    if data.get("rsi"):
        df = rsi_strategy(df, data["rsi"])
        strategy_used.append("RSI")
    if data.get("dca"):
        df = dca_strategy(df, data["dca"])
        strategy_used.append("DCA")
    if data.get("grid"):
        df = grid_strategy(df, data["grid"]["lower"], data["grid"]["upper"], data["grid"]["step"])
        strategy_used.append("GRID")
    if data.get("macd"):
        df = macd_strategy(df)
        strategy_used.append("MACD")

    trades, count = simulate(df)
    log_message(f"Simulated strategy: {strategy_used}, Trades: {count}")

    # ML decision
    acc = None
    if data.get("ml"):
        model, acc = train_model(df)
        log_message(f"ML Accuracy: {acc}")
        # ทดสอบว่า model ทำนาย "ขึ้น" จริงมั้ย
        last_row = df.iloc[-1][["open", "high", "low", "close", "volume"]].values.reshape(1, -1)
        prediction = model.predict(last_row)[0]
        log_message("AI says: BUY" if prediction else "AI says: HOLD")

    conn = sqlite3.connect("trading.db")
    c = conn.cursor()
    c.execute("INSERT INTO test_results (strategy, trades, accuracy) VALUES (?, ?, ?)",
              (",".join(strategy_used), count, acc))
    conn.commit()
    conn.close()

    return jsonify({
        "simulated_trades": count,
        "ml_accuracy": acc,
        "ai_action": "BUY" if acc and acc > 0.6 else "HOLD"
    })

if __name__ == "__main__":
    app.run(debug=True)
