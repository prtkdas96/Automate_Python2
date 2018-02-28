spam = [0,1,2,3,4,5]
cheese = spam
cheese[1] = 'Hello!'
print(cheese)
print(spam)
# Remember that any mutable file can never be stored in a variable.
# The variable contains only the reference to the mutable thingy.
def eggs(someParameter):
    someParameter.append('Hello')

spam = [1,2,3]
eggs(spam)
print(spam)
import copy
spam = ['A', 'B', 'C', 'D']
cheese = copy.deepcopy(spam)
cheese[1] = 42
print(cheese)
print(spam)
spam = ['apples',
        'oranges',
        'bananas',
        'cats']
print('Four score and seven' + \
      'years ago')
# The \ basically tells python that the line continues on the next line
# When passing a list argument to a function, you are actually passing a list reference
# Changes made to a list in a function will affect the list outside function
 


