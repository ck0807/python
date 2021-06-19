'''
#1

sum = 0
while True:
    for i in range(1,6):
        x = int(input("Please enter the scores: "))
        sum += x
        ave = sum/i
    print("the average of the five scores is:", sum/5)    
    reply = input("Do you like test them again?(y/n)")
    if reply == "n":
        break

#2
        
import random
row = int(input("Please enter the number of row: "))
column = int(input("Please enter the number of column: "))
for i in range(1,row+1):
    for j in range(1,column+1):
        num=random.randint(1,9)
        print(num,end='')
    print('')
'''
#3
for i in range (1,6):
    for j in range (1,6):
        if i==1 or i==5:
            print('1',end=' ')
        elif j==1 or j==5:
            print('1',end=' ')
        else:
            print('0',end=' ')
    print()

