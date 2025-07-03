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
3. Explain the role of self in a Python class. Can a method work without it? Give an example.

self represents the instance of the class

#self refers to the object(instance) of the class
then it can access/modify variables and methods from inside the class.

#without self we cannot tell to python which object data are you reffering
'''

class Person:
    def __init__(self, name):
        self.name = name
    def great(self):
        print(f"Hello {self.name}")

p = Person('praneeth')
p.great()



print('...................................................')
'''
4. Write a class Circle with a class variable pi = 3.14 and an instance variable radius.
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


print('...................................................')
'''
5. Differentiate between instance method, 
class method, and static method. Create a class that uses all three.
'''

#Instance Method: A method that uses self to access or modify object data.

#Class Method : A method that uses cls to access or modify class level data.

#Static Method : A method that does not use self or cls used for utility code inside a cls.

class Student:
    school_Name = " High school"
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:",self.name)
        print("Marks:",self.marks)

    @classmethod
    def display_school(cls):
        print("SchoolName is:",cls.school_Name)

    def display_notice():
        print("Sat is holiday")

s1 = Student("Praneeth", 100)

s1.display()
Student.display_school()
Student.display_notice()

print('....................................................')
'''
6. What is the output of the following code?

x = 5

def outer():
x = 10
def inner():
x = 15
print(“Inner:”, x)
inner()
print(“Outer:”, x)

outer()
print(“Global:”, x)
'''

x = 5
def outer():
    x = 10
    def inner():
        x = 15
        print("Inner is:", x)
    inner()
    print("Outer is:", x)
outer()
print("Global is:", x)


print('...................................................')
'''
7. What will the output be? Explain why.

x = 100

def modify():
global x
x = x + 50

modify()
print(x)
'''

x = 100

def modify():
    global x
    x = x + 50

modify()
print(x)

print('....................................')
'''
8. Create a nested function
 where a variable in the outer function is modified by the inner function using nonlocal.
'''
#NonLocal : it uses outer variable/count data...

def outer1():
    count = 0
    def inner():
        nonlocal count
        count += 1
        print("Inner count is:", count)
    inner()
    print("Outer count is:", count)

outer1()


print('.............................................')

'''
9. What does the dir(__builtins__) function return?
'''

#dir(__builtins__) function returns all the built-in functions of python which are no need to import
#ex: functions,print,int,range,len etc.......................

print(dir(__builtins__))

print('...............................................')

'''
10. Identify the scope of each x in the following code and explain the output.

x = “global”

def func1():
x = “enclosing”
def func2():
x = “local”
print(“func2:”, x)
func2()
print(“func1:”, x)

func1()
print(“global:”, x)
'''

x = 'global'

def func1():
    x = 'enclosing'
    def func2():
        x = 'local'
        print('fun2:', x)
    func2()
    print('fun1:', x)

func1()