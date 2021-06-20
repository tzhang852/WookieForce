#Create a calculator to show how long hero upgrades will take in real time
#based on Hero upgrade days and number of Builder Pots used

#number of hours heroes will take = length of hero upgrades - 10hours/pot

#?upgrade
# How long are your hero upgrades? 
    #return int - 2d 14 h
    #internal convert to 62 hours
    
# How many builder pots do you want to use?
    # return int - 3
        #27 hours
        #final calculation = hero - pot = 35
        #final return 1d 11 h

import sys
from typing import final
#convert string to int, read d as 24, multiply by number in front... delimiter = d?

#define constants
HOURS_PER_DAY = 24
#Hero conversion
while True:
    try:
        days=int(input("Enter number of days: "))
        #print("Number of days: ", days)
        hours=int(input("Enter number of hours: "))
        #print("Number of hours: ", hours)
        break;
    except ValueError:
        print("Invalid Input")

total_hours = days * HOURS_PER_DAY
total_hours = total_hours + hours
#print("Total hours for Hero Upgrades ", total_hours)

#Potion conversion
while True:
    try:
        potions = int(input("How many builder potions do you want to use?"))
        #print("Number of potions: ", potions)
        break;
    except ValueError:
        print("Invalid Input")

total_potion_hours = potions * 10
print(total_potion_hours)

#Final calculation
final_upgrade = total_hours - total_potion_hours - potions
print(final_upgrade)
if final_upgrade >= 24:
    final_days = final_upgrade % 24
    print(final_days)
    final_hours = final_upgrade - final_days*24
    print(final_hours)
print("Amount of time your hero upgrades will take: %sd %sh"% (final_days, final_hours))

#Potions = ((length of hero upgrade) - (time remaining in 1st war after attacks) + (Time remaining in 2nd war before attacks) - 48)/9

#Assume player has attacked already

#?war upgrade
    #first = How many hours are left in the current war?
    #return int - 18 h

    # How long are your hero upgrades?
    #return int - 2d 14h
    #internal convert to 62 hours

    #2nd attack
    #return int - 4h

    #final calculation = (hero - first + second - 48)/9
    #final return (always round up) 

# time is in Hrs

