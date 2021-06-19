'''
#1
nums =[]
for i in range (1,20,3):
    nums.append(i)

print(nums)
'''
'''
#2
nums=[0,0,0,0,0]
for i in range(len(nums)):
    nums[i] = i*i
print(nums)
'''
'''
#3
nums = [[1,3,5],[2,4,6],[3,5,7]]
for i in range(len(nums)):
    for j in range(len(nums[0])):
        nums[i][j] = nums[i][j]*2

print(nums)
'''
'''
#4
index = [1,3,5,7]
nums = ['a','b','c','d','e','f','g','h','i','j','k']
for i in index:
    print(nums[i])
'''
'''
#5
nums = [1,3,5,7,9,11,13]
nums_slice = nums[1:6:2]
nums_slice.reverse()
print(nums_slice)
'''
'''
#6
nums = [1,2,3,4,5,6]
for i in range(0,6,2):
    nums.insert(i,'a')

print(nums)
'''
'''
#7
import random
list = []
for i in range(0,101):
    x = random.randint(1,9)
    print(x)
'''
'''
#8
nums = [[10,30,50],[20,40,65],[35,55,70]]
for i in range(0, len(nums)):
    print(sum(nums[i]))

'''

'''
#1 
def main():

    user = input("Please enter a string: ")
    lower = 0
    upper = 0
    for ch in user:
        if ch.islower():
            lower += 1
        elif ch.isupper():
            upper += 1
        else:
            print("it has number or other element.")
    print("the upper case have: ", upper, "the lower case have: ", lower)

main()
'''
'''
#2 
def frac_vowel():
    n = 0
    m = 0
    text = input("please enter a sentance: ")
    for ch in text:
        if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u"\
           or ch == "A" or ch == "E" or ch == "I" or ch == "O" or ch == "U":
            m += 1
        else:
            n += 1 
            new = m + n
    print(m/new)
frac_vowel()
'''
#3
txt = input("please enter a senten: ")





