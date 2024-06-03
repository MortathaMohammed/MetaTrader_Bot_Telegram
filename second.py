import MetaTrader5 as mt5
import pandas as pd
import time
import numpy as np
from databace1 import Data as dt
from telegram_interface import send_msg_privet
from symbol import Symbols

symbol = "EURUSD"
n = 2
timeFrame = mt5.TIMEFRAME_M1
mt5.initialize()

def second(symbol = symbol, n = n, timeFrame = timeFrame):
    # print(symbol)
    rates = mt5.copy_rates_from_pos(symbol, timeFrame, 0, n)
    rates_frame = pd.DataFrame(rates)
    volume = 1
    fram_ko = int(rates_frame['tick_volume'].tail(1).values[0])
    close  = np.round(rates_frame['close'].tail(1).values[0], 5)
    
    if fram_ko >= int(volume):
        fram_ko = int(rates_frame['tick_volume'].tail(1).values[0])
    
        if volume > fram_ko:
            volume = 1
        else :
            if volume <= fram_ko:
                
                rates = mt5.copy_rates_from_pos(symbol, timeFrame, 0, n)
                rates_frame = pd.DataFrame(rates)
                last_volume = dt.find_info_second("second", symbol, volume, close)[1]
                last_close = dt.find_info_second("second", symbol, volume, close)[2]
                current_volume = fram_ko - volume
                current_close = rates_frame['close'].tail(1).values[0]

                # Increase = New Number - Original Number
                # % increase = Increase ÷ Original Number × 100
                increase_close = (current_close - last_close)
                chang_price = np.round((increase_close / last_close) * 100, 2)
                if last_volume > 0:
                    increase_volume = (current_volume - last_volume)
                    change_volume = np.round((increase_volume / last_volume) * 100, 2)
                else:
                    last_volume = 1
                    increase_volume = (current_volume - last_volume)
                    change_volume = np.round((increase_volume / last_volume) * 100, 2)

                # print(f"{close} : {new_close} : {chang_price}")
                # print((f"Last volume :{last_volume}\n\nCurrent volume :{current_volume}\nChange in volume :{change_volume}\n----------------\n"))
                # print((f"Last price :{close}\nCurrent Price :{current_close}\nChange in price :{chang_price}\n----------------\n"))
                
                # if current_volume > last_volume and current_volume > 10:
                    # send_msg_privet(f"Last volume :{last_volume}\n\nCurrent volume :{current_volume}")
                dt.save_info("second", symbol, current_volume, current_close)
                # print(rates_frame.tail(1))
                volume = fram_ko
                close  = current_close


