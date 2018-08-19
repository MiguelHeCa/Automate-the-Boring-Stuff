import re

message = 'Call me 415-555-1011 tomorrow, or at 415-555-9999'

# Search for just one pattern
# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo = phoneNumRegex.search(message)
# print(mo.group())

# Search for all patterns in a string

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneNumRegex.findall(message))
