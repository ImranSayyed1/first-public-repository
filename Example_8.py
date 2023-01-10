'''
Python doesn’t support method overloading like C++ or Java so we use class methods to create factory methods.
In the below example we use a class method to create a person object from birth year.
As explained above we use static methods to create utility functions. In the below example we use a static method to check if a person is an adult or not.
'''

# Difference between static method and class method

from datetime import date


class Person:
    name = ""
    age = ""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getname(self):
        return self.name

    def getage(self):
        return self.age

    # Utility method to check whether person is an adult or not
    @staticmethod
    def isAdult(age):
        return age > 18

    # Factory method to return an object of type Person
    @classmethod
    def getperson(cls, name, year):
        print("cls is\t", cls)
        return cls(name, date.today().year - year)


p1 = Person("Arun", 21)
print(p1.getname())
print(p1.getage())

print(Person.isAdult(13))

p2 = Person.getperson("Ganesh", 1990)
print(getattr(p2, 'name'))
print(getattr(p2, 'age'))
