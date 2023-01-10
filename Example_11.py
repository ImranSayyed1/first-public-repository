x=10
print(x)
print(type(x))

y=10
print(y)
print(type(y))

if id(x) == id(y):
    print("x and y refer to same int object")
else:
    print("x and y do not refer to same int object")

x=11
print(x)
print(type(x))

if id(x) == id(y):
    print("x and y refer to same int object")
else:
    print("x and y do not refer to same int object")