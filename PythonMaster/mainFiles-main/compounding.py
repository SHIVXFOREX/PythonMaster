import random
import time
from iqoptionapi.stable_api import IQ_Option
Iq=IQ_Option("shivxforex@gmail.com","IDEAPAD300")
Iq.connect()

print(Iq.check_connect())
balance_type="PRACTICE"
print(Iq.change_balance(balance_type))
print(Iq.get_balance())


ACTIVES="EURUSD"
duration=1#minute 1 or 5
default_Amt=10
amount=10
action="call"#put
polling_time=3
counter=1
expirations_mode=1
winCounter = 0 
lossCounter = 0
compundingAmt = 1

#check result 
def check_result(id):
  while True:
        check,win=Iq.check_win_digital_v2(id)
        if check==True:
            break
  if win<0:
        
        return win
  else:
        
        return win

#first time place trade
print("Placing First Trade!")
_,id=(Iq.buy_digital_spot(ACTIVES,amount,action,duration))


#Master Loop
while True:
    #MM 
    if check_result(id) > 0 :
      print("win")
      lossCounter = 0
      winCounter = winCounter + 1
      action = action
    else :
      print("loss")
      winCounter = 0
      lossCounter = lossCounter + 1
      if action == "put":
        action = "call" 
      else :
        action = "put"

    #AM
    if check_result(id) > 0 :
      if winCounter > 1 :
        amount = default_Amt
      if winCounter == 1 :
        amount = compundingAmt 
      else :
        amount = default_Amt
        print(compundingAmt)
    else :
        compundingAmt = compundingAmt + amount
        amount = default_Amt

    #Place Trade

    _,id=(Iq.buy_digital_spot(ACTIVES,amount,action,duration))

    #Counter Controller
  
    counter = counter + 1
    print("counter :- " + str(counter))
    print("Compounding Amt :- " + str(compundingAmt))
    print("WinCounter :- " +str(winCounter)) 
    print("LossCounter :- " +str(lossCounter)) 


