import random
import time
from iqoptionapi.stable_api import IQ_Option
Iq=IQ_Option("shivxforex@gmail.com","IDEAPAD300")
Iq.connect()

print(Iq.check_connect())
balance_type="PRACTICE"
print(Iq.change_balance(balance_type))
print(Iq.get_balance())

#variables
Martingle_Arr=[1,3,8,20,50,125,313,783,1956]
row1 = 0
row2 = 0
row3 = 0
row4 = 0 
row5 = 0

ACTIVES="EURUSD"
duration=1#minute 1 or 5
default_Amt=1
amount=1
action="call"#put
polling_time=3
counter=1
expirations_mode=1

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
_,id=(Iq.buy_digital_spot(ACTIVES,amount,action,duration))


#Master Loop
while True:
    #MM 
    if check_result(id) > 0 :
      action = action
    else :
      if action == "put":
        action = "call" 
      else :
        action = "put"
    
    #AM
    if counter == 1 :
      if check_result(id) > 0 :
        print("Win Row1")
        row1 = 0
      else :
        print("Loss Row1")
        row1 = row1 + 1
      amount = Martingle_Arr[row2]
      print("Amount Counter 1 :" + str(amount))
    elif counter == 2 :
      if check_result(id) > 0 :
        print("Win Row 2")
        row2 = 0
      else :
        print("Loss Row 2 ")
        row2 = row2 + 1
      amount = Martingle_Arr[row3]
      print("Amount Counter 2 :" + str(amount))
    elif counter == 3 :
      if check_result(id) > 0 :
        print("Win Row 3")
        row3 = 0
      else :
        print("Loss Row 3 ")
        row3 = row3 + 1
      amount = Martingle_Arr[row4]
      print("Amount Counter 3 :" + str(amount))
    elif counter == 4 :
      if check_result(id) > 0 :
        print("Win Row 4")
        row4 = 0
      else :
        print("Loss Row 4 ")
        row4 = row4 + 1
      amount = Martingle_Arr[row5]
      print("Amount Counter 4 :" + str(amount))
    elif counter == 5 :
      if check_result(id) > 0 :
        print("Win Row 5")
        row5 = 0
      else :
        print("Loss Row 5 ")
        row5 = row5 + 1
      amount = Martingle_Arr[row1]
      print("Amount Counter 5 :" + str(amount))
    
             
    
    #Place Trade

    _,id=(Iq.buy_digital_spot(ACTIVES,amount,action,duration))

    #Counter Controller
    if counter == 5 :
      counter = 1
      print("counter" + str(counter))
    else :
      counter = counter + 1
      print("counter" + str(counter)) 


