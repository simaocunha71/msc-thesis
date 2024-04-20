"""
Write a function to remove lowercase substrings from a given string.
assert remove_lowercase("PYTHon")==('PYTH')
"""

def remove_lowercase(s):
    for i in range(1,len(s),2):
        if s[i].islower():
            raise ValueError('Unwanted lowercased character found!')
    return s
