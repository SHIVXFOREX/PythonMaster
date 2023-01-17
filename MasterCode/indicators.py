import random
import time
from iqoptionapi.stable_api import IQ_Option
Iq=IQ_Option("shivxforex@gmail.com","IDEAPAD300")
Iq.connect()

print(Iq.check_connect())
balance_type="PRACTICE"

ACTIVES="EURUSD"
duration=1#minute 1 or 5
default_Amt=10
amount=10
action="call"#put
polling_time=3
counter=1
expirations_mode=1
sell = []
buy = []
hold = []

#Indicator Data
 
def indicato_fuction(curr):
    while True :
            sell = []
            buy = []
            hold = []
            asset=curr
            indicators = Iq.get_technical_indicators(asset)
            for x in indicators:
                if x['action'] == "sell" :
                    sell.append(x['action'])
                elif x['action'] == "buy" :
                    buy.append(x['action'])
                else :
                    hold.append(x['action'])
                    
            if len(buy) > len(sell) :
                if len(buy) > len(hold) :
                    print("action - buy")
                    return("action - buy")
                else :
                    print("action - hold")
                    return("action - hold")
            else :
                if len(sell) > len(hold) :
                    print("action - sELL")
                    return("action - Sell")
                else :
                    print("action - HOLD")
                    return("action - Hold")
                    
indicato_fuction("EURUSD")





