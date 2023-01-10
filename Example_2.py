class Student:
    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age


s1 = Student()
s1.setName("Sachin")
s1.setAge(30)
print(s1.getName(), "\t", s1.getAge())

s2 = Student()
s2.setName("Rahul")
s2.setAge(35)
print(s2.getName(), "\t", s2.getAge())
print("Let's print the contents of the class")
print(dir(Student))
