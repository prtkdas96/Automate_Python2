import re

batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search("The Adventures of Batman")
print(mo.group())
mo = batRegex.search("The Adventures of Batwoman")
print(mo.group())
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phone number is 415-555-1234. Call me tomorrow.')
print(mo.group())
mo = phoneRegex.search('My phone number is 555-2567. Call me tomorrow.')
mo == None
print(mo == None)
batRegex = re.compile(r'Bat(wo)+man')
mo2 = batRegex.search("The Adventures of Batwowowowowwowoman")
print(mo2 == None)
regex = re.compile(r'\+\*\?')
mo3 = regex.search('I learned about +*? regex syntax')
print(mo3 == None)
haRegex = re.compile(r'(Ha){3}')
mo4 = haRegex.search('He said "HaHaHa"')
print(mo4 == None)

haRegex = re.compile(r'(Ha){3,5}') # This indicate range. From 3 to 5 will match
mo5 = haRegex.search("He said 'HaHaHa'")
print(mo5 == None)
# Regular Expression in python matches the longest possible pattern that can be matched.
# They are kind of greedy
# To make it non greedy use ?
# For example digitregex = re.compile(r'(\d){3,5}?')

