'''
#i
sum1 = 0
sum2 = 0
while True:
    num = int(input("Please enter a number or enter 0 to stop: "))
    if num == 0:
        break
    if num >0:
        sum1 += num
    else:
        sum2 += num

print("The sum of all positive number is: ",sum1)
print("The sum of all negative number is: ",sum2)
'''
#ii
start = 8000
sum = 0
count = 0
amount = float(input("Please enter the amount you want to deposit: "))
print("Year","\t", "Balance")
print("-----------------------")
for year in range(1,16):
    count = amount *12 
    sum += count
    print(year,"\t", round(sum,2)+start)
print("The total balance is: ",start+round(sum,2))