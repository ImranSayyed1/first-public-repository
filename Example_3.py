# object.__dict__ is A dictionary or other mapping object used to store an object’s (writable) attributes

class Student:
    def __init__(self, name=None, age=0):  # constructor in Python
        self.name = name
        self.age = age

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def __str__(self):  # in order to print object in a readable format
        return self.name + "\t" + str(self.age)


s1 = Student()
s1.setName("Sachin")
s1.setAge(30)
print(s1.getName(), "\t", s1.getAge())

s2 = Student()
s2.setName("Rahul")
s2.setAge(35)
print(s2.getName(), "\t", s2.getAge())

s3 = Student("Anil", 40)
print(s3.getName(), "\t", s3.getAge())
print(s1.__dict__)
print("\n")
print(s1)
