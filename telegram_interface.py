import telepot
from datetime import datetime as dt
import requests
import MetaTrader5 as mt5
import pandas as pd
import numpy as np
from databace import Status as st

bot_token = "Your Token"
channel_chat_id = "Your channal Id"
my_chat_id = "your chat Id"


def time_now():
    time = dt.now()
    time = time.strftime("%H:%M:%S  //  %d-%m-%Y")
    return time


def account():
    account_info = mt5.account_info()
    if account_info != None:
        account_info_dict = mt5.account_info()._asdict()
        df = pd.DataFrame(list(account_info_dict.items()),
                          columns=['property', 'value'])
    return df


def balance():
    from_date = dt(2020, 1, 1)
    to_date = dt.now()

    # get deals for symbols whose names contain neither "EUR" nor "GBP"
    deals = mt5.history_deals_get(from_date, to_date)

    # display these deals as a table using pandas.DataFrame
    df = pd.DataFrame(list(deals), columns=deals[0]._asdict().keys())
    df['time'] = pd.to_datetime(df['time'], unit='s')
    return df.iloc[0, 13]


def profit_():
    from_date = dt(2020, 1, 1)
    to_date = dt.now()

    # get deals for symbols whose names contain neither "EUR" nor "GBP"
    deals = mt5.history_deals_get(from_date, to_date)

    # display these deals as a table using pandas.DataFrame
    df = pd.DataFrame(list(deals), columns=deals[0]._asdict().keys())
    df['time'] = pd.to_datetime(df['time'], unit='s')
    z = sum(df['profit'])
    return np.round(z - balance(), 1)


bot = telepot.Bot(bot_token)


def send_msg_privet(text):
    url = "https://api.telegram.org/bot"+bot_token + \
        "/sendMessage?chat_id="+my_chat_id+"&parse_mode=Markdown&text="
    request = url+text
    response = requests.get(request)
    return response.json()


def send_msg(text):
    url = "https://api.telegram.org/bot"+bot_token + \
        "/sendMessage?chat_id="+channel_chat_id+"&parse_mode=Markdown&text="
    request = url+text
    response = requests.get(request)
    return response.json()


def handle(msg):
    user_name = msg["from"]["first_name"]
    content_type, chat_typt, chat_id = telepot.glance(msg)
    if content_type == "text":
        my_command = msg["text"]

        if "START" in my_command.upper():
            bot.sendMessage(chat_id,
                            "Welcome "+user_name+" in your AutoTrafing bot! \n /help give you more information about your bot.")
        if "STATUS" in my_command.upper():
            stat = st.find_status(collection="status")
            bot.sendMessage(chat_id, "System is : " +
                            str(stat)+".", parse_mode="Markdown")

        elif "POSITIONS" in my_command.upper():
            positions = mt5.positions_total()
            bot.sendMessage(chat_id, "Active positions : " +
                            str(positions)+".", parse_mode="Markdown")

        elif "ON" in my_command.upper():
            st.save_status("status", my_command.upper(), time_now())
            with open("log.txt", "a") as log_file:
                log_file.write(f"System is activated at : {time_now()}\n")

        elif "OFF" in my_command.upper():
            st.save_status("status", my_command.upper(), time_now())
            with open("log.txt", "a") as log_file:
                log_file.write(f"System is disactivated at : {time_now()}\n")

        elif "BALANCE" in my_command.upper():
            balanc = account()
            bot.sendMessage(chat_id,
                            "Your balance is : `"+str(balanc.iloc[10][1])+" USD`", parse_mode="Markdown")

        elif "PROFITN" in my_command.upper():
            profit = account()
            bot.sendMessage(chat_id,
                            "Your profit from open positions is : `"+str(profit.iloc[12][1])+" USD`", parse_mode="Markdown")

        elif "DEPOSIT" in my_command.upper():
            deposit = balance()
            bot.sendMessage(chat_id,
                            "Your deposit is : `"+str(deposit)+" USD`", parse_mode="Markdown")

        elif "PROFITT" in my_command.upper():
            profit = profit_()
            bot.sendMessage(chat_id,
                            "Your total profit is : `"+str(profit)+" USD`", parse_mode="Markdown")

        elif "ORDERS" in my_command.upper():
            orders = mt5.orders_total()
            bot.sendMessage(chat_id, "Orders : "+str(orders) +
                            ".", parse_mode="Markdown")

        elif "/HELP" in my_command.upper():
            bot.sendMessage(
                chat_id, f"You can control the bot by [/ON , /OFF] command.\nTry:\n1. /Status\n2. /Deposit\n3. /Balance\n4. /ProfitT\n5. /ProfitN\n6. /Orders\n7. /Positions", parse_mode="Markdown")

        else:
            bot.sendMessage(
                chat_id, f"You can control the bot by [/ON , /OFF] command.\nTry:\n1. /Status\n2. /Deposit\n3. /Balance\n4. /ProfitT\n5. /ProfitN\n6. /Orders\n7. /Positions", parse_mode="Markdown")


bot.message_loop(handle)
