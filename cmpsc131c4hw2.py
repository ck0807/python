'''
#5,8,9,13,14 #8 only requires a while loop
#5 Average Rainfall
numYear = int(input("Please enter the number of year: ")) 
rainfall = 0
for year in range(numYear+1):
    for month in range(1, 13):
        MonthRainfall = float(input("Please enter the rainfall for eath month: "))
        rainfall += MonthRainfall
    ave = rainfall/month
    print("Month", "\t", "Rainfall")
    print("------------------------")

    for i in range(1,month+1):
        print(i, "\t", MonthRainfall)
    print("The numbber of year is:",numYear)
    print("This is the total number of rainfall",rainfall,"inches")
    print("The average for rainfall per month", round(ave,2),"inches")

#5 --while loop
rainfall = 0
month = 1

numYear = int(input("Please enter the number of year: ")) 
for year in range(numYear+1):
    while month < 3:
        MonthRainfall = float(input("Please enter the rainfall for eath month: "))
        rainfall += MonthRainfall
        month += 1
    ave = rainfall/(month-1)
print("The numbber of year is:",numYear)
print("This is the total number of rainfall",rainfall,"inches")
print("The average for rainfall per month", round(ave,2), "inches")


#8 Sum of Number
sumNum = 0
while True:
    num = float(input("Please enter positive number and enter a negative number to stop: "))
    if num < 0:
        break
    sumNum += num
print("You are program stop.")

print("The sum total of the number you input is:",sumNum)

#9 Ocean Levels
totalRise = 0
rise = 1.6
i = 1
while i <= 25:
    totalRise += rise
    i += 1
print("For next 25 year the number of millimeters that the ocean will have rissen", round(totalRise,2),"millimeters")    

#9 for loop
rise = 1.6
totalRise = 0
for i in range(1,26):
    totalRise += rise
    i += 1
print("For next 25 year the number of millimeters that the ocean will have rissen", round(totalRise,2),"millimeters")  


#13 Population
print("Day Approximate","\t","Population")
organisms = 2
aveIncrease = 0.3
for i in range(10):
    i += 1
    print(i,"\t\t\t", round(organisms,2))
    organisms *= (1 + aveIncrease)
 
#13 ---while
print("Day Approximate","\t","Population")
i = 0
organisms = 2
aveIncrease = 0.3
while i < 10:
    i += 1
    print(i,"\t\t\t", round(organisms,2))
    organisms *= (1 + aveIncrease)
 
#14 
for i in range(8,1,-1):
    for j in range(i):
        print("*",end="")
    print()

''' 
#14--while loop
i = 8   
while i > 1:
    i -= 1
    for j in range(i):
        print("*",end="")
    print()


    
    
    



    

   




