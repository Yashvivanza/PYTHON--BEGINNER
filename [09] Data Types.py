num = 2.5
print(type(num))
num1 = 5
print(type(num1))

# a + bj
num2 = 6 + 9j
print(type(num2))

# Convert Float to Integer
a = 5.6
b = int(a)
print(b)

# Covert Interger to FLoat
k = float(b)
print(k)
print("")

# Convert normal number to complex number
k = 6
c = complex(b,k)
print(c)
print("")

bool = b < k
print(bool)
print(type(bool))
print("")

print(int(True))
print(int(False))
print("")

lst=[25,36,45,12]
print(type(lst))

s = {12,14,25}
print(type(s))

t = (12,14,15,23)
print(type(t))
print("")

st = 'a'
print(type(st))
print("")

print(range(10))
print(list(range(10)))
print("")

print(list(range(2,11,2)))
print(type(range(11)))
print("")

# Mapping or Dictonary
d = {'navin':'samsung','rahul':'iphone','kiran':'Oneplus'}
print(d)
print("")
print(d.keys())
print(d.values())
print("")
print(d['rahul']) # in dictionary we cannot have an index number
print(d.get('rahul'))
print(d.get('kiran'))