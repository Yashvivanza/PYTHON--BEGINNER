nums = [25,12, 95]
print(nums)
print(nums[0])
print(nums[1])
print(nums[2])
print(nums[1:])
print(nums[-1])
print(nums[-3:-1])
print("")

names=['navin','kiran','john']
print(names)
print("")

values=[9.5,'Naivn',25]
print(values)
print("")

nums = [25,12, 95]
names=['navin','kiran','john']
mil = [nums,names]
print(mil)
print("")

nums = [25,12, 95]
nums.append(45) #  we can write direct value for adding element
print(nums)
print("")

nums.insert(2,23) # We declare index  while adding element
print(nums)
print("")

nums.remove(95) # We can delete  direct value from the list
print(nums)
print("")

nums.pop(1) # We declare index for deleting
print(nums)
print("")

nums.pop() # Here it deletes last element
print(nums)
print("")

del nums[1:] # how to delete multiply values
print(nums)
print("")

nums.extend([29,12,14,36])
print(nums)
print("")

print(min(nums))
print("")

print(max(nums))
print("")

print(sum(nums))
print("")

nums.sort()
print(nums)
