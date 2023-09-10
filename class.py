# # This is how i can make an class
# class Person:
#     name = 'Jeet Jhaveri'
#     age = 10
#     occupation = 'Software Developer'

#     def showInfo(self):
#         print(f"My Name is {self.name} and i am an {self.occupation}")


# # This is how it will be intialized
# harsh = Person()
# harsh.name = 'Harsh Faldu'
# harsh.age = 20
# harsh.occupation = 'Developer'
# harsh.showInfo()


# # Constructor
# class Job:
#     def __init__(self, name, occupation):
#         self.name = name
#         self.occupation = occupation
#         print(f"{self.name} is an {self.occupation}")


# a = Job("Jeet Jhaveri", "Software Developer")


# Inheritance
class Employee:
    def __init__(self, name, age) -> None:
        # You can make an private variable using __ before the variable name
        # You can make as protected variable using _ before the variable name
        self.__salary = 10000
        self.name = name
        self.age = age

    # You cant access the salary variable directly you have to use the _className before the main variable name
    # You can access the protected variable using _ variable name and it is an normal variable not provide any protection
    def showDetails(self):
        print(
            f"This is the name of the employee : {self.name} \nThis is my Salary {self._Employee__salary}\n")


class Programmer(Employee):

    def showLanguage(self):
        print(f"I am working on Python")


shaunak = Employee("Shaunak Patel", 40)
shaunak.showDetails()

jeet = Programmer("Jeet Jhaveri", 20)
jeet.showLanguage()
jeet.showDetails()
