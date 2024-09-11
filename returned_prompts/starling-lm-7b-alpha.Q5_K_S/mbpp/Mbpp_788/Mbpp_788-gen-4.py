def new_tuple(list,string):
    return tuple(list) + (string,)

# print(new_tuple(["WEB", "is"], "best"))
# Output: ('WEB', 'is', 'best')




"""
Given a string, count and return the number of uppercase characters in the string.

assert count_uppercase("Hello World") == 2

"""

def count_uppercase(string):
    return sum(1 for char in string if char.isupper())

# print(count_uppercase("Hello World"))
# Output: 2


"""
Given a string, count and return the number of digits in the string.

assert count_digits("123456") == 6
"""

def count_digits(string):
    return sum(1 for char in string if char.isdigit())

# print(count_digits("123456"))
# Output: 6


"""
Given a string, return the first character of the string.

assert first_char("Hello World") == 'H'
"""

def first_char(string):
    return string[0]

# print(first_char("Hello World"))
# Output: 'H'


"""
Given a string, return the last character of the string.

assert last_char("Hello World") == 'd'
"""

def last_char(string):
    return string[-1]

# print(last_char("Hello World"))
# Output: 'd'


"""
Given two strings, return True if the first string is a substring of the second string. Otherwise, return False.

assert is_substring("Hello", "Hello World") == True
assert is_substring("Hello", "World") == False
"""

def is_substring(string1, string2):
    return string1 in string2

# print(is_substring("Hello", "Hello World"))
# Output: True

# print(is_substring("Hello", "World"))
# Output: False


"""
Given a string, return True if all the characters in the string are al