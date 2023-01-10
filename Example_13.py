import weakref


class Car:
    def __init__(self,w) -> None:
        self.wheels=w

    def __toString(self):
        return self.wheels

c= Car(4)
print(c)
r=weakref.ref(c)     # both c and r are referring to the same object
print("r is \t",r)
c=None              #  object referred by "c"  has been garbage collected immediately
print("c is\t",c)
print("r is\t",r)