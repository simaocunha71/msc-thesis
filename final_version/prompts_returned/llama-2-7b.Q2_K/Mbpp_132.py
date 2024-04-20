"""
Write a function to convert a tuple to a string.
assert tup_string(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's'))==("exercises")
"""
from typing import List, Tuple
def tup_to_str(*t):
    return str(tuple(reversed(t))) # reverse string is more efficient, so use it.
assert tup_string(['a', 'b'])=='ab'
assert tup_to_str('hello') == 'heolloi'
assert tup_to_str(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's'))==("exercises")