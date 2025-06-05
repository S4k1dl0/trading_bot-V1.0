def simulate(df):
    trades = []
    for i in range(1, len(df)):
        if df['buy_signal'].iloc[i] and not df['buy_signal'].iloc[i - 1]:
            trades.append(df['close'].iloc[i])
    return trades, len(trades)
