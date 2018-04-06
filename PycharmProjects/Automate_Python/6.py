import re
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneRegex
Resume ='''
JESSE KENDALL
123 Elm Street, Fall River, MA 02723 Cell: 508-555-5555, Home: 508-555-1234

'''

phoneRegex.search(Resume)
phoneRegex.findall(Resume)

# findall returns a list of objects compared to search that returns a search object
phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
phoneRegex.findall(Resume)

# Using digitRegex
digitRegex = re.compile(r'\d')
digitRegex.findall(Resume)

lyrics = '12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing'
xmasRegex = re.compile(r'\d+\s+\w+')
xmasRegex.findall(lyrics)

vowelRegex = re.compile(r'[aeiouAEIOU]')
vowelRegex.findall("Robocop eats baby food.")
# The names indicate the function that the regular expression is carrying out
doubleVowelRegex = re.compile(r'[aeiouAEIOU]{2}')
doubleVowelRegex.findall("Robocop eats baby food.")

negativeRegex = re.compile(r'[^aeiouAEIOU]')
negativeRegex.findall("Robocop eats baby food")







