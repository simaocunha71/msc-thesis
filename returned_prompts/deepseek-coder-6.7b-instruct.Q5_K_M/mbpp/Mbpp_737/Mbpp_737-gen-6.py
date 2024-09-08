"""
Here is a simple python function using regex to check if the given string starts with a vowel or not.
"""

import re

def check_str(string):
    return bool(re.match(r'^[aeiou]', string, re.IGNORECASE))

# test the function
print(check_str("annie"))  # it should return True
"""

