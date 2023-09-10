# Simple Function
def subFunction(a, b):
    print("This is the answer of your substraction: ", a - b)


# An dynamic function
def addFuntion(*a):
    number = 0
    for numbers in a:
        number += numbers
    print("This is the answer of your addition : ", number)


# An function which create an dict as an argument
def studInformation(**information):
    print("\nStudent Information")
    print("-------------------")
    print("Student Name :", information['name'])
    print("Student Age :", information['age'])
    print("Student Number :", information['number'], '\n')


# A function that return a value or something
def name(name):
    return name


# Recursion
def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n-1)


addFuntion(5, 5)
subFunction(16, 10)
studInformation(name='Jeet Jhaveri', age=20, number=9712791515)
fullname = name('Jeet')
print(fullname)
print(factorial(3))
