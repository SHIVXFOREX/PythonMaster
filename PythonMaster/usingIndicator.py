import random
import time
from iqoptionapi.stable_api import IQ_Option
Iq=IQ_Option("shivxforex@gmail.com","IDEAPAD300")
Iq.connect()

print(Iq.check_connect())
balance_type="PRACTICE"
print(Iq.change_balance(balance_type))
print(Iq.get_balance())


ACTIVES="AUDUSD"
duration=1#minute 1 or 5
default_Amt=10
amount=10
action="call"#put
polling_time=3
counter=1
expirations_mode=1

#Indicator Data
asset="EURUSD"
indicators = Iq.get_technical_indicators(asset)
Stocastic = indicators[69]
print(Stocastic["action"])
print(Stocastic["group"])




