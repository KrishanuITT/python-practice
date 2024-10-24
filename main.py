print("Hello, World")

# Variables
price = 10  #Ineger
rating = 4.9 #Float
name = "Krishanu" #String
is_admin = True #Boolean
print(price)

# Input
name = input("Enter your name: ")
color = input("Enter your favourite color: ")
print(f"{name} likes {color} color.")

# Type Conversion
birth_year = input("Enter your birth year: ")
age = 2024 - int(birth_year)
print(age)
print(type(age))

# Strings
course = "Python's Course"
course = ''' 
    Hi. 
    How are you
'''
course = 'Python "Coding"'
print(course)
print(course[0])
print(course[-1])
print(course[0:3])
print(course[0:])
print(course[:5])
print(course[:])
print(len(course))
print(course.lower())
print(course.upper())
print(course.find("Coding"))
print(course.replace("Python", "Java"))

name = "Jeniffer"
print(name[1:-1])

first = "John"
last = 'Doe'

message =  first + " [" + last + "] is a coder"
msg = f"{first} [{last}] is a coder"
print(message)
print(msg)

# String Methods

course = 'Python for Beginners'
print(len(course))
# Methods
print(course.upper())
print(course.lower())
print(course.title())
print(course.find('P'))
print(course.replace('Beginners', 'Absolute Beginners'))
print('Python' in course)

# Operators

print(10+3)
print(10-3)
print(10*3)
print(10/3)
print(10//3)
print(10%3)
print(10**3)

x = 10
x = x+3
x+=3
print(x)

# Operator Precedence
x = 10 +3 * 2 ** 2
x = (10 + 3) * (2 ** 2)
print(x)

# Math Functions
x = 2.9
print(round(x))
print(abs(-2.9))

# Conditionals
is_hot = False
is_cold = True
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
else:
    print("Wear warm clothes")
print("Enjoy your day")

price = 1000000
has_good_credit = True
if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")


# Logical Operators
has_high_income = False
has_good_credit = True
if not has_high_income and has_good_credit:
    print("Eligible for loan")

# Comparison Operator
temprature = 30
if temprature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

name = input("Enter your name: ")
if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name must be a maximum of 50 characters")
else:
    print("Name looks good")

weight = input("Enter your weight: ")
method = input('(L)bs or (K)g: ')
if method.upper() == 'L':
    print(f"You are {weight} pounds")
elif method.upper() == 'K':
    print(f"You are {weight} kilos")
else:
    print("Invalid input")

# While Loop
i = 1
while i<=5:
    print('*' * i)
    i += 1
print("Done")

# Game
secret_number = 9

while True:
    guess = int(input("Guess: "))
    if guess == secret_number:
        print("You won!")
        break
    else:
        print("Try again")

while True:
    command = input('>')
    if command.lower() == 'start':
        print('Car started...')
    elif command.lower() == 'stop':
        print('Car stopped')
    elif command.lower() == 'quit':
        break
    elif command.lower() == 'help':
        print('''\tstart - to start the car  
        stop - to stop the car
        quit - to exit''')
    else:
        print("Sorry, I don't understand that...")

# For Loop
for item in 'Python':
    print(item)

for item in range(10):
    print(item+1)

price = [10,20,30]
total = 0

for item in price:
    total += item
print(total)

# Nested Loop
for x in range(4):
    for y in range(3):
        print(f'({x}, {y})', end=' ')
    print()

number = [5, 2, 5, 2, 2]
for x in range(len(number)):
    print('x' * number[x])

# Lists
names = ['John', 'Corey', 'Adam', 'Steve']
print(names)
print(names[0])
print(names[:3])

num = [1,2,3,10,3,4,8]
max = 0
for i in num:
    if i > max:
        max = i
print(max)

# 2D Lists

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]]
print(matrix)
print(matrix[1])

for row in matrix:
    for item in row:
        print(item, end=' ')
    print('')

numbers = [1,2,3,4,5,6,7]
numbers.append(8)
numbers.insert(0,10)
numbers.remove(1)
number2 = numbers.copy()
number2.sort()
number2.reverse()
print(number2)
numbers.pop()
numbers.clear()
print(numbers)

# Remove Duplicates from List:
list = [1,3,4,4,3,4,6,7,7]
new_list = []

for item in list:
    if item not in new_list:
        new_list.append(item)
print(new_list)

# Tuples
coordinates = (1,2,1)
print(coordinates.count(10))
print(coordinates.__add__((2,3)))

coordinates = (1,2,3)
x, y, z = coordinates

# Dictionaries
customer = {
    "name": "John",
    "age": 30,
    "is_verified": True
}
print(customer['age'])
print(customer.get('b'))


phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero",
}

output = ""
for ch in phone:
    print(digits_mapping[ch], end=" ")

# Functions
def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome Aboard")


print('Start')
greet_user("John", "Smith")
print('End')
greet_user(first_name="John", last_name="Smith")

def square(num):
    return num * num

print(square(5))

# Exceptions
try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
except ValueError:
    print("Invalid value")
except ZeroDivisionError:
    print("Age cannot be 0")


# Classes

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print(self.x,self.y)


point1 = Point(10, 20)
point = Point()
point1.draw()
point.draw()

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


john = Person("John Smith")
john.talk()

# Inheritance

class Animal:
    def walk(self):
        print("animal - walk")
class Dog(Animal):
    pass

class Cat(Animal):
    def walk(self):
        print("cat - walk")


dog1 = Dog()
cat1 = Cat()
dog1.walk()
cat1.walk()

from modules.converters import kg_to_lbs
print(kg_to_lbs(10))