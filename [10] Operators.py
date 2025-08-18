x = 2
y = 3
print( x + y)
print( x - y)
print( x * y)
print( x / y)
print( x % y)
print( x ** y)
print( x // y)
print(" ")

x = x + 2
print(x)
x += 2
print(x)
x *= 3
print(x)
print("")

a,b = 5,6
print(a)
print(b)
print(a,b)
print("")

# Unary Operator
n = 7
print(n)
-n
print(n)
n = -n
print(n)
print("")

# Relational Operators
print(a<b)
print(a>b)
print(a==b) # '=' means we are assigning values in python and '==' means we are comparing.
a = 6
print(a==b)
b = 7
print(a!=b)
print("")

# Logical Operators
a = 5
b = 4
print(a<8 and b<5)
print(a<8 and b<2)
print(a<8 or b<2)
print("")
x = True
print(x)
x = not x
print(x)