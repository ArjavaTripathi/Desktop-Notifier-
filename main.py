from datetime import datetime, timedelta
import re 
import sys
import time 

timeremind = str(input("In what intervals would you like to get notified? (xx hour xx minutes): "))

timingslist = []





    
timingslist.append(timeremind.split()[0])
timingslist.append(timeremind.split()[2])

hourtoseconds = int(timingslist[0]) * 3600
minutestoseconds = int(timingslist[1]) * 60
totaltime = hourtoseconds + minutestoseconds

print(totaltime)

Done = True

while Done:
    print("NOTIFICATION")
    time.sleep(totaltime)

"""current_time = now.strftime("%H:%M:%S")
#print("Current Time =", current_time) get current time 
timings["StartTime"] = now.strftime("%H:%M")


timenow = now.strftime("%H:%M")

print(timenow)



print(timings)

input("Enter any key to quit... ")
sys.exit()"""



 
