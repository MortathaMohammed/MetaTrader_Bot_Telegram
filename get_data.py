import MetaTrader5 as mt5
import pandas as pd
import numpy as np
import datetime as df
from orders_mt5 import *


def get_data(symbol, n, timeframe = mt5.TIMEFRAME_M1):
        ''' Function to import data of the chosen symbol '''
        
        # Initializ the connection if ther is not
        mt5.initialize()

        # Import the data into a tuple
        rates = mt5.copy_rates_from_pos(symbol, timeframe, 1, n)
    

        # Tuple to dataframe
        rates_frame = pd.DataFrame(rates)
        
        # Convert time in seconds into the datatime fromat
        rates_frame['time'] = pd.to_datetime(rates_frame['time'], unit = 's')

        # # Convert the column "time" in the right format
        rates_frame['time'] = pd.to_datetime(rates_frame['time'], format = '%y-%m-%d')

        # Set column time as the index of the dataframe
        rates_frame = rates_frame.set_index('time')
  
        return rates_frame

def get_ticks(symbol, n):
    ''' Function to import data of the chosen symbol '''
    
    # Initializ the connection if ther is not
    mt5.initialize()

    # Current data extract
    utc_from = df.now()

    # Import the data into a tuple
    ticks = mt5.copy_ticks_from(symbol, utc_from, n, mt5.COPY_TICKS_ALL)
 

    # Tuple to dataframe
    ticks_frame = pd.DataFrame(ticks)
    
    # Convert time in seconds into the datatime fromat
    ticks_frame['time'] = pd.to_datetime(ticks_frame['time'], unit = 's')

    # Convert the column "time" in the right format
    ticks_frame['time'] = pd.to_datetime(ticks_frame['time'], format = '%y-%m-%d')

    # Set column time as the index of the dataframe
    ticks_frame = ticks_frame.set_index('time')
    return ticks_frame



def get_data_s(symbol, n, timeframe = mt5.TIMEFRAME_M1):
        ''' Function to import data of the chosen symbol '''
        
        # Initializ the connection if ther is not
        mt5.initialize()

        # Import the data into a tuple
        rates = mt5.copy_rates_from_pos(symbol, timeframe, 1, n)
    
        # Tuple to dataframe
        rates_frame = pd.DataFrame(rates)
        
        # Convert time in seconds into the datatime fromat
        rates_frame['time'] = pd.to_datetime(rates_frame['time'], unit = 's')

        # Convert the column "time" in the right format
        rates_frame['time'] = pd.to_datetime(rates_frame['time'], format = '%y-%m-%d')

        # Set column time as the index of the dataframe
        rates_frame = rates_frame.set_index('time')
  
        return rates_frame