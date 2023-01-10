var1=10
var2=10   # both var1 and var2 refer to same object which has a value 10

print(var1)
print(var2)
print(type(var1))
print(type(var2))

# proof that var1 and var2 refer to same memory address
print(hex(id(var1)))
print(hex(id(var1)))