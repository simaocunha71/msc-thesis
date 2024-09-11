"""
Here is a Python program that uses regex to check if a given string starts with a vowel:

import re

def check_str(s):
    if re.match("^[aeiouAEIOU]", s):
        return True
    else:
        return False

# Test the function
print(check_str("annie"))  # Returns True
print(check_str("amy"))    # Returns True
print(check_str("amanda")) # Returns False
"""

In this program, the `check_str` function is used to determine whether a string starts with a vowel. The `re.match` function is used to match the string against a regular expression pattern. The pattern `^[aeiouAEIOU]` ensures that the string starts with any of the vowels, both lower case and upper case. If the pattern matches, the function returns `True`; otherwise, it returns `False`.

To test the function, you can use the `print` statement to display the result of the function for different strings. For example, `print(check_str("annie"))` will print `True` because "annie" starts with a vowel, and `print(check_str("amy"))` will also print `True` for the same reason. However, `print(check_str("amanda"))` will print `False` because "amanda" does not start with a vowel.

By using this program, you can easily check if a string starts with a vowel using regex in Python.



The provided solution uses the `re` module in Python, which is the built-in regular expression module. The `re.match` function is used to match the string against a regular expression pattern. In this case, the pattern `^[aeiouAEIOU]` is used to match the string at the beginning (`^`) of the string and ensures that the string starts with any of the vowels, both lower case and upper case.

The `re.match` function returns a match object if the string matches the pattern, and `None` if it does not. The function `check_str` uses this match object to determine whether the string starts with a vowel. If the match object is not `None`, the function returns `