from tkinter.tix import Tree
import MetaTrader5 as mt5

def login( account = int(5006090387), password = "qe3dycze", server = "MetaQuotes-Demo"):
     
    if not mt5.initialize(login=account, password = password, server = server):
        return False

    authorized=mt5.login(account, password, server)

    if authorized:
        return True
    else:
        return True


# Name     : Mortaza Mortaza
# Type     : Forex Hedged USD
# Server   : MetaQuotes-Demo
# Login    : 5006090387
# Password : qe3dycze
# Investor : dj8bgejg

