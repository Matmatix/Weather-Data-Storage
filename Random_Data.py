#Random data generation for the hash table
#Generating data for 3 locations: Milwaukee (53201), New York (10001), Detroit (48127)

from random import *

write = open("data.txt", "w")

for loc in range(3):
    for day in range(365):
        if (day/30) == 0:     #temps for january
            temp = 22.5
            variation = 13.5
            month = "01"
            day = (day % 30)
        elif (day/30) == 1:    #Febraury
            temp = 25.5
            variation = 13
            month = "02"
            day = (day % 30)
        elif day/30 == 2:    #March
            temp = 35.5 
            variation = 13
            month = "03"
            day = (day % 30)
        elif day/30 == 3:    #April
            temp = 45
            variation = 14
            month = "04"
            day = (day % 30)
        elif day/30 == 4:    #May
            temp = 56
            variation = 16
            month = "05"
            day = (day % 30)
        elif day/30 == 5:    #June
            temp = 65
            variation = 16
            month = "06"
            day = (day % 30)
        elif day/30 == 6:    #July
            temp = 71.5
            variation = 15
            month = "07"
            day = (day % 30)
        elif day/30 == 7:    #August
            temp = 71
            variation = 14
            month = "08"
            day = (day % 30)
        elif day/30 == 8:    #September
            temp = 63.5
            variation = 15
            month = "09"
            day = (day % 30)
        elif day/30 == 9:    #October
            temp = 51
            variation = 14
            month = "10"
            day = (day % 30)
        elif day/30 == 10:    #November
            temp = 39
            variation = 12
            month = "11"
            day = (day % 30)
        elif day/30 == 11:    #December
            temp = 27
            variation = 12
            month = "12"
            day = (day % 30)

        rand = .01 * randint(0, 101)    #Generate percentage offset
        if randint(0, 2) == 0:           #positive or negative increase
            rand *= -1
        
        temp = temp + (variation * rand)    #Caculcate temperature

        rand = randint(0, 2)            #Get rand to determine weather

        if rand == 0:                 #raining, foggy, or sunny
            if temp < 32:
                weather = "snowing"
            else: 
                weather = "raining"
        elif rand == 1:
            weather = "foggy"
        else: 
            weather = "sunny"

        if loc == 0: 
            location = "53201"
        elif loc == 1:
            location = "10001"
        else: 
            location = "48127"

        key = location + month + str(day) + "18"
        data = key + "," + str(int(temp)) + "," + weather + "\n"

        write.write(data)

write.close()


