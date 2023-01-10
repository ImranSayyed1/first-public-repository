""" In Python, everything is dynamically bound, and since you can add members to an instance, not all instances
of
the same class are guaranteed to have the same members. """


class First:
    def __init__(self, num1):
        self.num1 = num1


f1 = First(100)
print(f1.num1)
print(dir(f1))

print("Let's create another object")
f2 = First(200)
print(f2.num1)
f2.num2 = 300
print(f2.num2)
print(dir(f2))
