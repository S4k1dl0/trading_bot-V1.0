def dca_strategy(df, interval=3):
    df['dca_signal'] = False
    for i in range(0, len(df), interval):
        df.at[df.index[i], 'dca_signal'] = True
    return df

def grid_strategy(df, lower=68000, upper=70000, step=500):
    df['grid_signal'] = df['close'].apply(lambda x: lower <= x <= upper and (x - lower) % step == 0)
    return df

import pandas_ta as ta

def macd_strategy(df):
    macd = ta.macd(df['close'])
    df = df.join(macd)
    df['macd_signal'] = (df['MACD_12_26_9'] > df['MACDs_12_26_9'])
    return df
