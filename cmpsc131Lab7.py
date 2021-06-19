'''
#1
def func1():
    print('here1')
def func2():
    print('here2')
    func1()
def func3():
    func2()
    func1()
func2()
func3()

#2
def func1(x):
    for i in range(5):
        print(i * x)

func1(3)

#3
def func1(x):
    return x*2
def func2(x):
    x+=2
    return func1(x)
result = func2(5)
print(result)

#4
def main():
    x = 4
    y = 10
    z = 2
    func1(y, z, x)
def func1(x, y, z):
    print(x / y + z)
main()

#5
def func1(x):
    for i in range(2,x):
        print(func2(i))
def func2(num):
    return num**num
func1(5)
'''
'''
#1Write a function print_many(x) that has one parameter that expects an
#integer and prints out ‘hello’ that many times.
def print_many(x):
    for i in range(x):
        print("hello")
print_many(5)
'''
#2 Write a function valid_score(score) that returns True if the given
#score is in the range between 0 and 100 inclusive otherwise it returns False
def main():
    score = int(input("Please enter a number between 0 and 100: "))
    valid_score(score)
def valid_score(score):
    if score < 0 or score > 100:
        return 'False'
    else:
        return 'True'
    result = valid_score(score)
    print(result)
main()
#3 Write a function called fizz_buzz(num) that takes an integer as a parameter.
#  If the number is divisible by 3, it should return “Fizz”.
#  If it is divisible by 5, it should return “Buzz”.
#  If it is divisible by both 3 and 5, it should return “FizzBuzz”.
#  Otherwise, it should return the same number.
def main():
    fb_var = int(input("pllease enter an integer: "))
    result = fizz_buzz(fb_var)
    print(result)
def fizz_buzz(num):
    if num%3 == 0 and num%5 ==0:
        return "FizzBuzz"
    elif num%3 == 0:
        return "Fizz"
    elif num%5 ==0:
        return "Buzz"
    else:
        return num