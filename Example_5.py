# no need to define setter and getters in Python as we have getattr and setattr in built methods
class MyClass:
    name = ""
    age = ""

    def __init__(self, name, age):
        self.name = name
        self.age = age


m = MyClass("Arun", 20)
print(getattr(m, 'name'))
print(getattr(m, 'age'))

setattr(m, 'name', "Vishal")
setattr(m, 'age', 35)

print(getattr(m, 'name'))
print(getattr(m, 'age'))
