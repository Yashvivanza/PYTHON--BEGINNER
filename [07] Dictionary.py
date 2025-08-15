data = {1:'Navin',2:'Kiran',4:'Harsh'}
print(data)
print("")

print(data[4])
print("")

print(data[1])
print("")

# print(data[3]) - error

print(data.get(1))
print("")

print(data.get(3)) # Now this time we didn't get error
print("")

print(data.get(1,'Not Found'))
print("")

print(data.get(3,'Not Found'))
print("")

# Now We will create Dictionary with the help of List
keys = ['Navin','Kiran','Harsh']
values = ['Python','Java','JS']
print(keys,values)
print("")

data1 = zip(keys,values)
data1 = dict(zip(keys,values))
print(data1)
print("")

# So now I want to add new value then
data1['Monica'] = 'CS'
print(data1)
print("")

data1.pop('Harsh')
print(data1)
print("")

#  Put a List inside a dictionary as a value and putting dictionary inside a dicionary
prog = {'JS':'Atom', 'CS': 'VS','Python':['Pycharm','Sublime'],'Java':{'JSE':'Netbeans','JEE':'Eclipse'}}
print(prog)
print("")

print(prog['JS'])
print(prog['CS'])
print(prog['Python'])
print(prog['Python'][1])
print(prog['Java'])