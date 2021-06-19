'''
#1
i = 0
while i <= 5:
    print(i)
    i = i + 1
'''
'''
#2
i = 1
while i<10:
    print(i)
    i = i + 3
'''
'''
#3
i = 50
while i <= 65:
    print('hello')
    i = 1 + 5
'''
'''
#4
i = 90
while i > 85:
    print(i)
    i = i - 2
'''
'''
#5
i = 1
while i <= 6:
    if i > 3:
        print(i)
    else:
        print("*")
    i = i + 1

#6
total = 0
i = 1
while i < 10:
    total =total + i
    i = i + 2

print(total)
'''
'''
#7
i = 1
while i <= 5:
    if i % 2 ==0:
        print("x")
    else:
        print("y")
    i = i + 1
'''
'''
#8
i = 10
while i <= 100:
    print(i)
    i = i * 2
    '''
'''
#9
num = 2
i = 10
while i < 17:
    print(1+num)
    i = i + 2
    '''
'''    
#1 Write a while loop that prints out the numbers 10, 11, 12, ..., 19, 20

i = 10
while i <= 20:
    print(i)
    i = i + 1
'''
'''
#2 Write a while loop that prints out the numbers 100, 150, 200, 250, …, 1000

i = 100
while i <= 1000:
    print(i)
    i = i + 50
'''

'''
#3 Write a while loop that prints out the numbers 50, 48, 46, 44, …, 30
i = 50
while i >= 30:
    print(i)
    i = i - 2 
'''
'''
#4 Write a while loop that sums up all the numbers between 1000 and 2000
sum = 0
i = 1000
while i <= 2000:
    sum = sum + i
    i = i + 1
    
print('the total is: ', sum)
'''
#5  Write a while loop that displays the square roots of all the odd numbers
#between 1 and 100. 
i = 1
while i < 100:
    i = i + 1
    if i % 2 != 0:
        newi = i * i
        print(newi)
        