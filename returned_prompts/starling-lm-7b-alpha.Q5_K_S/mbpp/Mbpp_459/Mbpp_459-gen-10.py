def remove_uppercase(s):
    return "".join(ch for ch in s if ch.islower())

# Alternative solution using regex
import re
def remove_uppercase_alt(s):
    return re.sub(r'[A-Z]', '', s)

# Testing
print(remove_uppercase('cAstyoUrFavoRitETVshoWs')) # 'cstyoravoitshos'
print(remove_uppercase_alt('cAstyoUrFavoRitETVshoWs')) # 'cstyoravoitshos'

# Another approach
def remove_uppercase_another(s):
    return ''.join(c for c in s if c.islower())

# Testing
print(remove_uppercase_another('cAstyoUrFavoRitETVshoWs')) # 'cstyoravoitshos'






"""
Python has a built-in function called `.join()` that concatenates all the strings in an iterable (like a list) into a single string. In this case, we are joining all the characters that are lowercase.

The `.lower()` function is a built-in function that will convert a string to all lowercase.

The `.isupper()` function will return True if the string is all uppercase, and False if it is not. In this case, we use the `.isupper()` function to determine if the string is uppercase or not.

The `.islower()` function is similar to `.isupper()`, but it returns True if the string is all lowercase, and False if it is not.
"""

# Python 3.x code
def remove_uppercase(s):
    return ''.join(ch for ch in s if ch.islower())

# Testing
print(remove_uppercase('cAstyoUrFavoRitETVshoWs')) # 'cstyoravoitshos'

# Another approach
def remove_uppercase_another(s):
    return ''.join(c for c in s if c.islower())

#