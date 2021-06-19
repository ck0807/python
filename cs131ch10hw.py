'''

#1
class Pet:
    def __init__(self, n, t, g):
        self.name = n
        self.animal_tpye = t
        self.age = g
    
    def set_name(self,n):
        self.name = n

    def set_animal_tpye(self, t):
        self.animal_tpye = t

    def set_age(self, g):
        self.age = g
    
    def get_name(self):
        return self.name

    def get_animal_tpye(self):
        return self.animal_tpye

    def get_age(self):
        return self.age

def main():
    name = input("please enter yout pet'name: ")
    animal_type = input("Please enter your pet's type: ")
    age = int(input("Please enter your prt's age: "))
    my_pet = Pet(name, animal_type, age)
    print("My pet'name is: ", my_pet.get_name(), "the animal type is: ", my_pet.get_animal_tpye(), "the age is: ", my_pet.get_age())

main()
'''
'''
#2
class Car:
    def __init__(self, y, m):
        self.year = y
        self.make = m
        self.speed = 0
        
    def set_year(self,y):
        self.year = y

    def set_make(self,m):
        self.make = m
   

    def accelerate(self,a):
        self.speed += 5 * a

    def brake(self,b):
        self.speed -= 5 * b

    def get_speed(self):
        return self.speed
    
    def __str__(self):
        return "the year is " + str(self.year) + "\n make is " + self.make + "\n speed is " + str(self.speed)
def main():
    year = int(input("please enter the year of model: "))
    make = input("Please enter the make of car: ")
    #speed = float(input("please enter the speed"))
    my_car = Car(year, make)
    my_car.accelerate(5)
    print(my_car.__str__())
    my_car.brake(5)
    print("After 5 time breke, the speed is: ", my_car.get_speed())
main()
'''
'''
#3
class info:
    def __init__(self,name, address, age, phone):
        self._name = name
        self._address = address
        self._age = age
        self._phone = phone
    def set_name(self,name):
        self._name = name
    def set_address(self,address):
        self._address = address
    def set_age(self, age):
        self._age = age
    def set_phone(self, phone):
        self._phone = phone
    def get_name(self):
        return self._name
    def get_address(self):
        return self._address
    def get_age(self):
        return self._age
    def get_phone(self):
        return self._phone
    def __str__(self):
        return "Name: " + self._name + "\n address: " + self._address + "\n age: " + self._age + "\n phone number: " + self._phone


def main():
    my = info("Xingping", "boston", "18", "857-111-2222")
    print("My info: \n", my)
    friend = info("Amy", "Malden", "19", "617-222-3333")
    print("My friend's info: \n", friend)
    family = info("Chris", "Quincy", "20", "857-333-4444")
    print("My family member's info: \n", family)
main()

'''
class Employee:
    def __init__(self, n, num, d, j):
        self.name = n
        self.id_number = num
        self.department = d
        self.job_title = j
    def set_name(self, n):
        self.name = n
    def set_id_number(self, num):
        self.id_number = num
    def set_department(self, d):
        self.department = d
    def set_job_title(self, j):
        self.job_title= j
    def get_name(self):
        return self.name
    def get_id_number(self):
        return self.id_number
    def get_department(self):
        return self.department
    def get_job_title(self):
        return self.job_title

    def __str__(self):
        return str(self.name) + " " + str(self.id_number) + " " + str(self.department) +  " " + str(self.job_title)


def main():
    em01 = Employee("Susan Meyers", "47899", "Acoounting", "Vice president")
    em02 = Employee("Mark", "39119", "IT", "Programmer") 
    em03 = Employee("Joy Rgers", "81774", "Manufacturing", "Engineer")
    #print(em01.get_name(), "  ", em01.get_id_number(), "  ", em01.get_department(), " ", em01.get_job_title())
    print(em01)
    print(em02)
    print(em03)

main()
    
    


