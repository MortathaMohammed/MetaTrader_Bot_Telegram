from cmath import e
import time
from tkinter import E
import MetaTrader5 as mt5
from databace1 import Status as st
from datetime import datetime as dt
from login import login
from telegram_interface import send_msg_privet
from second import second
from symbol import Symbols

def time_now():
    time  = dt.now()
    time = time.strftime("%H:%M:%S  //  %d-%m-%Y")
    return time

x = 0
y = 0

while True:
    try:

        stat = st.find_status(collection="status")
        while "/ON" in stat or "ON" in stat:
            if x == 0:
                y = 0
                send_msg_privet(f"systme actvated at : {time_now()}")
                if login() == True:
                    send_msg_privet("Meta Trader server is : Connected ")
                else:
                    send_msg_privet("Meta Trader server is : Disconnected !!!")
            x = 1
            print("Start")
            for symbol in Symbols:

                second(symbol)
            print("End")
            stat = st.find_status(collection="status")
            time.sleep(0.99)
            
            
        if y == 0:
            x = 0
            send_msg_privet(f"systme disactvated at : {time_now()}")
            if mt5.shutdown():
                send_msg_privet("Meta Trader shutdown !!!")

            y = 1
    except:
        pass
    time.sleep(5)