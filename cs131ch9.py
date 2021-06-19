'''
#1 Write a program that creates a dictionary containing the U.S. states as keys,
#  and their capitals as values. The program should randomly quiz the user by 
# displaying the name of a state and asking the user to enter the state's
# capital. The program will ask 5 questions and keep a count of the number of 
# correct and incorrect responses. You can use the following dictionary:
import random

capital_dic={ 'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona':'Phoenix',\
     'Arkansas':'Little Rock', 'California': 'Sacramento', 'Colorado':'Denver', \
    'Connecticut':'Hartford', 'Delaware':'Dover', 'Florida': 'Tallahassee', \
    'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinios': 'Springfield', \
    'Indiana': 'Indianapolis', 'Iowa': 'Des Monies', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', \
    'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', \
    'Michigan': 'Lansing', 'Minnesota': 'St. Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', \
    'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Neveda': 'Carson City', 'New Hampshire': 'Concord', \
    'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',\
    'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', \
    'Pennsylvania': 'Harrisburg', 'Rhoda Island': 'Providence', 'South Carolina': 'Columbia', \
    'South Dakoda': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', \
    'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', \
    'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne' }
correct = 0
incorrect = 0
count = 0
while count <= 5:
    state = random.choice(list(capital_dic))
    user = input("What is the capital of " + state + "is: ")
    if user == capital_dic[state]:
        correct += 1
    else:
        incorrect += 1
    count += 1
print("The correct answer is: ", str(correct))
print("The incorrect answer is: ", str(incorrect))
'''
'''
#2 Write a program that uses a dictionary to assign "codes" to each letter of the alphabet. For example:
# codes = { 'a' : '!', 'b' : '*', 'c' : '(', 'd' : '&', ..., etc}
# You can choose what symbol/number/other letter will represent each letter
# Using this example the letter a would be assigned the symbol !, the letter b would be assigned * and so forth.
# Ask the user to enter a string and using your codes dictionary translate the string into symbols.

codes = { 'a' : '!', 'b' : '*', 'c' : '(', 'd' : '&', 'e' : '@', 'f' : '#', 'g' : '$', 'h' : '%', \
          'i' : '^', 'j' : ')', 'k' : '-', 'l' : '_', 'm' : '+', 'n' : '=', 'o' : '~', 'p' : '`', \
          'q' : '1', 'r' : '2', 's' : '3', 't' : '4', 'u' : '5', 'v' : '6', 'w' : '7', 'x' : '8', \
          'y' : '9', 'z' : '0'}

user = input("Please enter your string: ")

print("The symbols are: ", codes[user])
'''
'''
#3 Write a program that asks a user to enter a sentence then display all the unique words in that string.
# Hint: Store each word as an element of a set
sentence = input("Please enter a sentence: ")
s = sentence.split()
print(s)
'''

# 4 Change my modified card_dealer.py file attached to this post to make it deal 5 cards to 4 players. 
# The program should determine which hand is worth the most and let us know who the winner is. 
# please see card_dealer(1)