import re

pattern = re.compile('(0|1)*1(0|1)*1(0|1)*1(0|1)*')

def match_string(s):
    return bool(pattern.fullmatch(s))

# Test
print(match_string('1110'))   # True
print(match_string('101011')) # True
print(match_string('0110'))  # False