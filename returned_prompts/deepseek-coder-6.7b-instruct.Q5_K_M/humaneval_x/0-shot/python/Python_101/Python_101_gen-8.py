
def words_string(s):
    return s.replace(',', '').split()

print(words_string("Hi, my name is John"))
print(words_string("One, two, three, four, five, six"))


def words_string(s):
    return [i for i in s.replace(',', '').split()]

print(words_string("Hi, my name is John"))
print(words_string("One, two, three, four, five, six"))


def words_string(s):
    return s.replace(' ', '').split(',')

print(words_string("Hi, my name is John"))
print(words_string("One, two, three, four, five, six"))


def words_string(s):
    return [i for i in s.replace(' ', '').split(',')]

print(words_string("Hi, my name is John"))
print(words_string("One, two, three, four, five, six"))

All of these solutions do the same thing. They take a string s and split it into words by removing commas or spaces. The first part of the string is separated by a comma and the second part is separated by spaces. 

The first solution uses the built-in string method replace() to remove the commas, and then the split() method to split the string into words. The result is a list of words.

The second solution uses a list comprehension to achieve the same result.

The third and fourth solutions use the replace() method to remove spaces, and then split() method to split the string into words. The result is a list of words.

The fourth solution uses a list comprehension to achieve the same result.
'''

# Code:

def words_string(s):
    return [i for i in s.replace(',', '').split()]

print(words_string("Hi, my name is John"))
print(words_string("One, two, three, four, five, six"))


'''
Output:

['Hi', 'my', 'name', 'is', 'John']
['One', 'two', 'three', 'four', 'five', 'six']