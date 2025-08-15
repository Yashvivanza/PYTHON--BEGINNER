# It is simply a collection of unique elements.
# here the answer is always direct , because it has hash values.
s = {22,25,14,21,5}
sorted_list = sorted(list(s))
print(sorted_list)

# s[2] - in set indexing is not supported.
s.discard(14)
print(s)

s.add(10)
print(s)