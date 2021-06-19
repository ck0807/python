'''
#1
d = {0:0, 1:0, 2:0, 3:0}
for i in d:
    d[i] += 10
print(d)
'''
'''
#2
d = {'a':5, 'b':10, 'c':15}
total = 0
for i in d:
    total += d[i]*2
print(total)
'''
'''
#3
d = {"P":1, "A":2, "H":3, "R":4, "O":5}
for c in "AOR":
    print(d[c])
'''
'''
#4
d = {}
for i in range(1, 11, 3):
    d[i] = i+3
print(d)
'''
'''
#1
n = int(input("Please enter a integer: "))
d = {}
for i in range(1, n+1):
    d[i] = i * i
print(d)
'''
#2
string = input("Please enter some string: ")
count = {}
for i in string:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
print("Count the string is:", str(count))



