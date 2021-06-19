#10, 11, 12, 13, 14, 15, 17, 18, 20, 21
'''
#10 Feet to Inches
def feet_to_inches():
    inches = int(input("please enter the inches to caculate the feet: "))
    feet = 12 * inches
    print("There is",feet, "equals", inches)
feet_to_inches()


#11 Math quiz
import random
def main():
    
    num1 = random.randint(0,1000)
    num2 = random.randint(0,1000)
    print("\t", num1, "\n", "+", "\t", num2)
    print("---------------------")
    result = float(input("Result: "))
    if result == num1 + num2:
        print("Congratulations!")
    else:
        print("The correct answer is", num1+num2)
main()
'''
'''
#12 Maximum of two values
def main():
    num1 = int(input("Please enter a integer: "))
    num2 = int(input("Please enter another integer: "))
    print("The greater one is", max(num1,num2))
    max(num1,num2)
def max(num1,num2):
    
    if num1 > num2:
        return num1
    else:
        return num2
    
main()
'''
'''
#13 Falling Distance
def main():
    for t in range(1,11):
        distance = falling_distance(t)
        print(t, round(distance,2))

def falling_distance(t):
    g = 9.8
    d =(1/2) * g * (t ** 2)
    return d
main()
'''
'''
#14 Kinetic Energy
def main():
    m = float(input("Please enter the mass(in kilograms): "))
    v = float(input("Please enter the velocity(in meter per second): "))
    
    print(kinetic_energy(m,v),"is the object's kinetic energy.")

def kinetic_energy(m,v):
    ke = 0.5 * m * v ** 2
    return ke
main()
'''
'''
#15 Test Average and Grade
score1 = float(input("Please enter the test one score: "))
score2 = float(input("Please enter the test two score: "))
score3 = float(input("Please enter the test three score: "))
score4 = float(input("Please enter the test four score: "))
score5 = float(input("Please enter the test five score: "))
print("Score", "\t", "Letter Grade")
print("-------------------------------")
def calc_average(score1, score2, score3, score4, score5):
    ave = (score1 + score2 + score3 + score4 + score5) / 5
    return ave
    
def determine_grade(score1, score2, score3, score4, score5):
    for i in score1, score2, score3, score4, score5:
        if i >= 90:
            print(i, "\t\t", "A")
        elif i >= 80 and i <= 89:
            print(i, "\t\t", "B")
        elif i >= 70 and i <= 79:
            print(i, "\t\t", "C")
        elif i >= 60 and i <= 69:
            print(i, "\t\t", "D")
        elif i < 60:
            print(i, "\t\t", "F")
        else:
            print("invaild score") 
    

  
ave = calc_average(score1, score2, score3, score4, score5)

determine_grade(score1, score2, score3, score4, score5)
print("The average of test score is: ", ave)
'''
'''
#17 Prime Numbers

def main():
    n = int(input("Please enter a integer number if is prime will return true, not prime will return false:: "))
    result = is_prime(n)
    print(n, result)

def is_prime(n):
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    else:
        return True
main()
'''
'''
#18 Prime Number List
print("number", "\t", "is prime.")
print("--------------------------")
def main():

    for i in range(2,101):
        result =  is_prime(i) 
        if result == 1:
            print(str(i), "is prime") 

def is_prime(n):
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return 0
    else:
        return 1
main()
'''
'''
#20 Random number guessing game
import random 
print("Please guess number from 1 to 100: ")
n = random.randrange(100) + 1
while True:
    guess = int(input("Please enter your guess: "))
    if guess == n:
        print("Congrats, you won!")
        print("Restarting game.")
    elif guess < n:
        print("too low, try again.")
    else:
        print("too hight, try again.")
'''
#21 Rock, paper, scissors game
import random
def main():
    player_rps = player_random_choice()
    while player_rps != "Rock" and player_rps != "Paper" and player_rps != "Scissors":
        player_rps = player_random_choice()

    rpsgame = random_number()
    computer_rps = computer_random_choice(rpsgame)

    print('Computer''s choice: ', computer_rps)

    while ((player_rps == "Rock" and computer_rps == "Rock") or
           (player_rps == "Paper" and computer_rps == "Paper") or
           (player_rps == "Scissors" and computer_rps == "Scissors")):
        print('You Both Tied. Play Again')
        print()
        player_rps = player_random_choice()
        rpsgame = random_number()
        computer_rps = computer_random_choice(rpsgame)
        print('Computer''s choice: ', computer_rps)

    computerplayer_game(player_rps, computer_rps)

def random_number():
    rpsgame = random.randint(1, 3)
    return rpsgame

def computer_random_choice(rpsgame):
    computer_rps = ""
    if rpsgame == 1:
        computer_rps = "Rock"

    elif rpsgame == 2:
        computer_rps = "Paper"

    elif rpsgame == 3:
        computer_rps = "Scissors"

    return computer_rps


def player_random_choice():
    player_rps = input('Enter the following choices, Rock, Paper, or Scissors:')
    return player_rps

def computerplayer_game(player_rps, computer_rps):

    if player_rps == "Rock" and computer_rps == "Paper":
        print('You Lose. Sorry Try Again')

    elif player_rps == "Paper" and computer_rps == "Rock":
        print('Congratulations!!! You Won The Game')

    elif player_rps == "Scissors" and computer_rps == "Rock":
        print('You Lose. Sorry Try Again')

    elif player_rps == "Rock" and computer_rps == "Scissors":
        print('Congratulations!!! You Won The Game')

    elif player_rps == "Paper" and computer_rps == "Scissors":
        print('You Lose. Sorry Try Again')

    elif player_rps == "Scissors" and computer_rps == "Paper":
        print('Congratulations!!! You Won The Game')


main()

 












