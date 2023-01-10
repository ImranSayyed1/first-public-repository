class Car:
    wheels=0
    def __init__(self,wheels):
        self.wheels=wheels
    def getwheels(self):
        return self.wheels


c1= Car(4)
print(c1)
print(c1.getwheels())
c2=c1   # both c1 and c2 refer to same object of Car
print(hex(id(c1)))
print(hex(id(c1)))
