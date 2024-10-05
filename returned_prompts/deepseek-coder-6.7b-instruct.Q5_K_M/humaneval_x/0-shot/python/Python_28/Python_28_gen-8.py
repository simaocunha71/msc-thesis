from typing import List

def concatenate(strings: List[str]) -> str:
    return ''.join(strings)

print(concatenate([])) # ''
print(concatenate(['a', 'b', 'c'])) # 'abc'

# List comprehension
def concatenate(strings: List[str]) -> str:
    return ''.join([s for s in strings])

print(concatenate([])) # ''
print(concatenate(['a', 'b', 'c'])) # 'abc'

# Map function
def concatenate(strings: List[str]) -> str:
    return ''.join(map(str, strings))

print(concatenate([])) # ''
print(concatenate(['a', 'b', 'c'])) # 'abc'

# Using reduce function
from functools import reduce
def concatenate(strings: List[str]) -> str:
    return reduce((lambda s, t: s + t), strings)

print(concatenate([])) # ''
print(concatenate(['a', 'b', 'c'])) # 'abc'
"""


"""
