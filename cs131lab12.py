'''
#1
import math
class Circle:
    def __init__(self, r):
        self.__radius = r

    def set_radius(self, r):
        r = int(input("please enter the radius: "))
        self.__radius = r

    def get_radius(self):
        return self.__radius

    def area(self):
        return self.__radius ** 2 * math.pi

    def perimeter(self):
        return 2 * self.__radius * math.pi


    def __str__(self):
        return "The radius of the circle is " + str(self.__radius)

def main():
    my_c = Circle(3)
    my_c.set_radius(3)
    print(my_c.get_radius())
    print("area: ", my_c.area())
    print("perimeter: ", my_c.perimeter())
main()
'''
#2
class Book:
    def __init__(self, t, a, p):
        self.__title = t
        self.__author = a
        self.__publisher = p
    def set_title(self, t):
        
        self.__title = t
    def set_author(self, a):
        self.__author = a
    def set_publisher(self,p):
        self.__publisher = p
    def get_title(self):
        return self.__title
    def get_author(self):
        return self.__author
    def get_publisher(self):
        return self.__publisher
    def __str__(self):
        return "The title is " + self.__title + "\n The authoris: " + self.__author + "\n The publisher is " +  self.__publisher
        
def main():
    my_book = Book("boo1", "amy", "mike")
    print(my_book)
main()









