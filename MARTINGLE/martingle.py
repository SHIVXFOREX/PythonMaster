
import masterlist
    
#variables
#Martingle_Arr=[1,1,1,1,3,3,3,8,8,8,20,20,50,125,783,783,2461]
#Martingle_Arr=[1,3,6,14,30,60,150,300,600,1200,2400]
#Martingle_Arr=[3,6,14,30,60,150,300,600,1200,2400,4800,300,150,60,600]
#Martingle_Arr=[ 1, 4, 7, 10, 13, 16, 19, 22, 25,30,35]
#Martingle_Arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#Martingle_Arr = [1.6,1,8,0,3,3,9,8,8,7,4,9,8,9,4,8,4,8,2,0,4,5,8,6,8,3,4,3,6,5,6,3,8,1,1,7,7,2,0,3,0,9,1,7,9,8,0,5,7,6,2,8,6,2,1,3,5,4,4,8,6,2,2,7,0,5,2,6,0,4,6,2,8,1,8,9,0,2,4,4,9,7,0,7,2,0,7,2,0,4,1,8,9,3,9,1,1,3,7,4]
#13700Martingle_Arr = [53,12,94,46,16,53,51,38,58,50,28,41,46,12,60]
#138365 Martingle_Arr = [867,407,784,111,700,532,12,984,417,871,948,879,117,831,926]
#Martingle_Arr =[2,1,3,4,7,11,18,29,47,76,123,199,322,521,843]
#78000
#120400 
#13500 Martingle_Arr = [914,302,678,55,387,532,763,798,198,181,505,839,580,185,745]
#129500 Martingle_Arr = [914,302,678,55,387,532,463,498,198,181,505,439,580,185,745]
#139500 Martingle_Arr = [1014,302,678,55,387,532,463,498,198,181,505,439,580,185,745]
#47000 Martingle_Arr = [331,140,462,279,88,384,237,375,308,299,363,150,79,114,322]
#65000 Martingle_Arr = [631,140,462,279,88,384,237,375,308,299,363,150,79,114,322]
#10000 Martingle_Arr = [10,1,8,27,64,125,216,343,512,729,1000,1331,1728,2197,27

#40000 Martingle_Arr = [510,1,8,27,64,125,216,343,512,729,1000,1331,1728,2197,2744]
#52000 
#45000 Martingle_Arr = [710,1,8,27,64,125,216,343,512,729,10,8,3,9,8]
#40000 Martingle_Arr = [503,12,94,46,16,53,51,38,58,50,28,41,46,12,60]
#53000 Martingle_Arr = [713,12,94,46,16,53,51,38,58,50,28,41,46,12,60]
#22000 Martingle_Arr = [200,12,94,46,16,53,51,38,58,50,28,41,46,12,60]
Martingle_Arr = [713,12,94,46,16,53,51,38,58,50,28,41,46,12,60]

row1 = 0
row2 = 0
row3 = 0
row4 = 0 
row5 = 0
row6 = 0
row7 = 0
row8 = 0
row9 = 0 
row10= 0


default_Amt=1
amount=1
counter=1
amount_list = []
action = "GREEN"
lossCounter = 0
winCounter = 0
result = ""
total_Amt = 0
final_win = 0


for x in masterlist.list_oct_nov_dec:    
    #MM 
    if x == action :
        print("WIN")
        result = "WIN"
        lossCounter = 0
        winCounter = winCounter + 1
        action = action
        final_win = final_win + amount
    else :
        print("LOSS")
        result = "LOSS"
        winCounter = 0
        lossCounter = lossCounter + 1
        final_win = final_win - amount
        if action == "GREEN" :
           action = "RED"
        else :
           action = "GREEN"

   #AM
    if counter == 1 :
      if result == "WIN" :
        print("Win Row1")
        row1 = 0
      else :
        print("Loss Row1")
        row1 = row1 + 1
      amount = Martingle_Arr[row1]
      print("Amount Counter 1 :" + str(amount))

    amount_list.append(amount)
    total_Amt = total_Amt + amount


    if counter == 1 :
      counter = 1
      print("counter" + str(counter))
    else :
      counter = counter + 1
      print("counter" + str(counter)) 

print(total_Amt)
print(final_win)
print(max(amount_list))
    
          