'''
#1 
for i in range(1,4):
    for j in range(1,4):
        print(j)

#2
for i in range(1,4):
    for j in range(1,4):
        print(i)

#3
i = 0
while i < 3:
    print(i)
    for j in range(1,2):
        print("inner")
    i += 1

#4
total = 0
for i in range(0,2):
    j = 1
    while j > 4:
        total += j
        j += 1
print(total)

#5
for i in range(3):
    for j in range(4):
        print('*', end='')
    print('')

#6 
total = 0
for i in range(1,4):
    for j in range(1,3):
        total = total + i + j

print(total)
'''
#1 nested loop
for i in range(0,3):
    for j in range(1,5):
        print(j,end='')
    print('')
#2
for i in range(3):
    for i in range(2):
        print('#',end='')
    print('')

#3
for i in range(1,5):
    for j in range(1,4):
        print(i,end='')
    print('')
