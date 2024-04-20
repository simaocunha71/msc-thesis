"""
Write a python function to find the first repeated character in a given string.
assert first_repeated_char("abcabc") == "a"
"""
import re
def first_repeated_char(str):
    if type(str) is not str:
        raise TypeError('arg must be of type str or list of strings')

    if len(str) <= 1:
        return ''

    if type(str) == str and type(str[0]) != str:
        str = str[0]

    for i in range(len(str)):
        c, d, s = re.split('([a-z])', str[i])
        if not c or len(d) <= 1:
            continue
        
        return first_repeated_char(s)
    else:
        raise ValueError('arg must be of type list of strings')
