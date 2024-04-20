"""
Write a function to replace all spaces in the given string with '%20'.
assert replace_spaces("My Name is Dawood") == 'My%20Name%20is%20Dawood'
"""
from typing import List, Optional

def replace_spaces(string: str):
    """Replace all spaces in a given string with '%20'. """
    
    return "%20".join([x for x in string.split() if len(x) > 1])
