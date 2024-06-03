import pandas as pd
import numpy as np
import pandas_ta as ta

def vwapZscore(pds, data):
    mean = vwap(pds,data=data)
    vwapsd = np.sqrt(ta.sma(pow(data['close'] - mean, 2), pds))
    return (data['close'] - mean )/vwapsd

def vwap(pds, data):
    return np.round(ta.sma((data['tick_volume'] * (data['low'] + data['high'] + data['close'])/3),pds) / ta.sma(data['tick_volume'], pds),2)

def stdvwap(pds, data):
    mean = vwap(pds,data=data)
    return np.sqrt(ta.sma(pow(data['close'] - mean, 2), pds))

def adr(pds, data):
    dr = data.apply(lambda x: x['high'] - x['low'], axis = 1)
    return dr.rolling(pds).mean()

def adr_pc(pds, data):
    dr_pc = data.apply(lambda x: 100 * (x['high'] / x['low'] - 1), axis = 1)
    return dr_pc.rolling(pds).mean()

def atr(pds, data):
    high_low = data['high'] - data['low']
    high_cp = np.abs(data['high'] - data['close'].shift())
    low_cp = np.abs(data['low'] - data['close'].shift())
    df = pd.concat([high_low, high_cp, low_cp], axis = 1)
    true_range = np.max(df, axis = 1)
    average_true_range = true_range.rolling(pds).mean()
    return average_true_range
