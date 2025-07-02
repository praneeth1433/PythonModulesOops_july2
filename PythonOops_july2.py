'''
#OOPS

1. Write a Python class named Employee with instance variables name and salary.
Add a constructor to initialize them and a method display() to print details.
'''
import math


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display(self):
        print("Name:",self.name)
        print("Salary:",self.salary)

emp1 = Employee("Praneeth", 20000)
emp2 = Employee("Mirai", 25000)
emp1.display()
emp2.display()



print('...................................................')
'''
2. What will be the output of the following code?

class Test:
def __init__(self, x):
self.x = x

a = Test(10)
b = Test(20)
print(a.x)
print(b.x)
'''

class Test:
    def __init__(self, x):
        self.x = x
a = Test(10)
b = Test(20)
print(a.x)
print(b.x)


print('...................................................')

'''
Explain the role of self in a Python class. Can a method work without it? Give an example.

self represents the instance of the class
'''

class Person:
    def __init__(self, name):
        self.name = name
    def great(self):
        print(f"Hello {self.name}")

p = Person('praneeth')
p.great()

'''
Write a class Circle with a class variable pi = 3.14 and an instance variable radius.
 Add a method to calculate area
'''

class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.pi * self.radius * self.radius

c1= Circle(5)
print("Area of a circle is:",c1.area())


