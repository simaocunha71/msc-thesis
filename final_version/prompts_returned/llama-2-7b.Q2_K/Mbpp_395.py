"""
Write a python function to find the first non-repeated character in a given string.
assert first_non_repeating_character("abcabc") == None
"""
import re

def first_non_repeated(s):
    try:
        for i, c in enumerate(s, start=1):
            if i == len(s) or c != s[i-1]:
                return c
    except StopIteration as e:
        print("The string doesn't have any characters!")
    assert not e
    