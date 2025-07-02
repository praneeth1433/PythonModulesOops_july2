'''
 1: Create and Use a Simple Module
Create a module calc.py with functions add, subtract, multiply, and divide
Import it into another script and perform all operations.
'''

# importing from cal.py

import calc
print(calc.subtract(2, 3))

from calc import add, subtract, multiply, divide

print(add(1, 2))
print(subtract(2, 3))
print(multiply(2, 3))
print(divide(2, 3))



'''
 2: Build a Geometry Toolkit
Create a file geometry.py with functions to calculate:
Area and perimeter of a circle
Area and perimeter of a rectangle
Use it in a separate file to display the results for given inputs.
'''


#importing from geometry.py


from geometry import circle_area, circle_perimeter, rectangle_perimeter, rectangle_area

r = 5

print('area of a circle:',circle_area(r))
print('perimeter of a circle:',circle_perimeter(r))

l = 6
w = 8

print('area of a rectangle:',rectangle_area(l,w))
print('perimeter of a rectangle',rectangle_perimeter(l,w))

'''
Task 3: Use Built-in Modules
Use the following modules:
math – to find square roots and factorials.
random – to generate random passwords.
datetime – to calculate age from date of birth.
'''

import math
import random
from datetime import datetime

num = 25

print("square root of ",num," is ",math.sqrt(num))
print("factorial of ",num," is ",math.factorial(num))

letters = "abcdefghij@#$%1234567890"
password = "".join(random.sample(letters,8))
print("random password is ",password)

dob = "2000-08-24"
dob_date = datetime.strptime(dob, "%Y-%m-%d")
today = datetime.today()
age = today.year - dob_date.year

if (today.month, today.day) < (dob_date.month, dob_date.day):
    age -= 1
print("age ",age)


'''
 4: Directory Analyzer
Use the os module to:
List all files in a directory
Count how many .py files are present
Create a new folder named backup
'''

import os

files = os.listdir("C:/Users/SSD/PycharmProjects/PythonProjectDemo")
print("all files and folders :")
for f in files:
    print(f)

count = 0
for f in files:
    if f.endswith('.py'):
        count += 1

print("count of .py files :",count)

if not os.path.exists('backup'):
    os.mkdir('backup')
    print("created backup")
else:
    print("backup folder already exists")

'''
 5: Reload Module During Development
Create a module temp.py with a simple function.
Import and use it in another script.
Change the function in temp.py, then reload the module using importlib.
'''

import temp
import importlib

#temp.greeting()
#here the 1st greeting will print

importlib.reload(temp)
#here the 2nd greeting which was updated later is print
temp.greeting()

