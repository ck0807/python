#1,2,5,8,11
'''
#1 Initials
n = input("Please enter your First, middle, and last name: ")
n = n.upper()
name = n.split()
print("The initials are:", name[0][0], ".", name[1][0], ".", name[2][0])
'''
'''

#2 Sum of Digits a String
numString = input("Please enter a series of single-digit number: ")
transInt = int(numString)
total = 0
while transInt:
    total += transInt % 10
    transInt = transInt // 10

print(total)
'''
'''
#5 Alphabetic Telephone Number Translator
phone = input("please enter the number in the format of '555-GET-FOOD': ")
newNum = ''
for i in phone:
    if i == 'A' or i == 'B' or i == 'C':
     i = '2'
    elif i == 'D' or i == 'E' or i == 'F':
     i = '3'
    elif i == 'G' or i == 'H' or i == 'I':
     i = '4'
    elif i == 'J' or i == 'K' or i == 'L':
     i = '5'
    elif i == 'M' or i == 'N' or i == 'O':
     i = '6'
    elif i == 'P' or i == 'Q' or i == 'R' or i == 'S':
     i = '7'
    elif i == 'T' or i == 'U' or i == 'V':
     i = '8'
    elif i == 'W' or i == 'X' or i == 'Y' or i == 'Z':
     i = '9'
    newNum = newNum + i

print("The number will be:", newNum)
'''
'''

#8 Sentence Capitalizer
string = input("Please enter your string: ")
newString = string[0].upper()
i = 1

while i < len(string)-2:
    newString += string[i]
    if string[i] == '.' or string[i] == '?' or string[i] == '!':
        newString += ' '
        newString += string[i+2].upper()
        i = i+3
    else:
        if i == len(string)-3:
            newString += string[len(string)-2:len(string)]
        i = i+1

print(newString)
'''

#11 Word Separator
sen = input("Please enter a string: ")
newSen = sen[0].upper()
for i in sen[1:]:
    if i.isupper():
        newSen += " "+ i.lower()
    else:
        newSen += i

print(newSen)



