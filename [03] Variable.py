x= 2
print(x + 3)

y = 3
print(x + y)

x= 9
print(x + y)

print(x)

# print(abc) - error

result = x + 10
print(result)
print(result + y)
print("")

name = 'youtube'
print(name)
name1 = name + ' rocks'
print(name1)
print("")

print(name[0])
print(name[1])
# print(name[8]) - error
print(name[-1])
print(name[-7])
print("")

print(name[0:2]) # Answer would be (yo) not (you) because 2 is not counted.
print(name[1:4])
print(name[-6:-2 ])
print(name[1:])
print(name[:4])
print(name[3:10])
print("")

# name[0:3] = "my"
# print(name)
"""string in Python is immutable"""

name2 = 'my ' + name[3:]
print(name2)
print("")

''' Length'''
myname = "Navin Reddy"
print(len(myname))