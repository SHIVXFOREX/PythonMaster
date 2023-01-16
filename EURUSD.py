#CHANGE VERSON 2
#verson 8 
#LINUX SERVER
#lINUX sWWERVRS 2
from datetime import datetime
import time
from iqoptionapi.stable_api import IQ_Option

while True :
    time.sleep(1)
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    seconds = now.strftime("%H:%M:%S")
    print("min and sec =", seconds)
    if seconds == "11:21:00" :
        print("time is 06:31:00")
        error_password="""{"code":"invalid_credentials","message":"You entered the wrong credentials. Please check that the login/password is correct."}"""
        Iq=IQ_Option("shivxforex@gmail.com","IDEAPAD300")
        check,reason=Iq.connect()

        if check:
            print("Start your robot")
            #if see this you can close network for test
            balance_type="PRACTICE"
            print(Iq.change_balance(balance_type))
            print(Iq.get_balance())
            


            ACTIVES="EURUSD"
            duration=1#minute 1 or 5
            default_Amt=1
            amount=1
            action="call"#put
            polling_time=3
            counter=1
            expirations_mode=1
            winCounter = 0 
            lossCounter = 0
            compundingAmt = 1
            firstCompound = True

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
                file1 = open("EURUSD.txt", "a")
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
                    print("ACTION1")
                    action = "call" 
                 else :
                    print("ACTION2")
                    action = "put"

                #AM
                if check_result(id) > 0 :
                 if winCounter > 1 :
                    firstCompound = True
                    compundingAmt = default_Amt
                    amount = default_Amt
                 if winCounter == 1 :
                    amount = compundingAmt * 0.19 + compundingAmt
                 else :
                    amount = default_Amt * 0.19 + default_Amt
                    print(compundingAmt)
                else :
                    compundingAmt = compundingAmt + amount
                    amount = default_Amt * 0.19 + default_Amt
                #Place Trade
                if firstCompound :
                    if compundingAmt > 100 :
                        firstCompound = False
                        print("Sleeping for 30 Min")
                        time.sleep(1800)

                _,id=(Iq.buy_digital_spot(ACTIVES,amount,action,duration))

                #Counter Controller
            
                counter = counter + 1
                print("-------------------------------------")
                print("Counter :- " + str(counter))
                print("Compounding Amt :- " + str(compundingAmt))
                print("WinCounter :- " +str(winCounter)) 
                print("LossCounter :- " +str(lossCounter))
                print("Balance :- " , Iq.get_balance()) 
                print("Amount :- " , amount)
                print("-------------------------------------")
                file1.write("T&D :- " + dt_string + " | ")
                file1.write(ACTIVES + " | ")
                file1.write(action + " | ")
                file1.write(str(amount))
                file1.write(" | Counter :- " + str(counter) + " | ")
                file1.write(str(Iq.get_balance()))
                file1.write(" | Compounding Amt :- " + str(compundingAmt)+ "\n")
                #file1.write( + " " + ACTIVES + " " + action + " Amount :- " , amount , " counter :- " + str(counter) + " Compounding Amt :- " + str(compundingAmt) + " Balance :- " , Iq.get_balance() , "  \n")
                file1.close()
        
    