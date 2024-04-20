"""
Write a python function to convert the given string to lower case.
assert is_lower("InValid") == "invalid"
"""
import re

def is_lower(s):
    if s not in_list:
        return re.sub('^[A-Z]+', '_' * (len(s)), s)
    else:
        return s

in_list = ['a', 'b', 'c']