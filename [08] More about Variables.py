num = 5
print(id(num))
print("")

name = 'Navin'
print(id(name))
print("")

#In python when we create multiple varailbes and in case they have same datta they both will point to the same address (box).
a = 10
b = a
print(a)
print(b)
print(id(a))
print(id(b))
print("")

print(id(10)) # Address is not based on the variable name , it is based on boxes itself.
print("")

k = 10
print(id(k))
print("")

a = 9
print(id(a))
print(id(b))
print("")

k = a
print(id(k))
print("")
# So here 
# a -> 9
# b -> 10
# k -> 9

PI = 3.14
print(PI)
PI = 3.15
print(PI)
print("")

# How to know the type of varaible
print(type(PI))