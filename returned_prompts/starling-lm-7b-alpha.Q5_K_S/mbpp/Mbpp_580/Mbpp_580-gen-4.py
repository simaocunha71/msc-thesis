"""
Here's one approach to solve this problem:

1. Iterate over the given tuple.
2. Check if the current element is a tuple. If so, call the function recursively on that tuple and append the result to a new list. If the current element is not a tuple, check if it's an even number. If so, append it to the new list.
3. Return the new list.

Here's a Python function that implements this approach:

def extract_even(t):
    even = []
    for elem in t:
        if isinstance(elem, tuple):
            even.append(extract_even(elem))
        else:
            if elem % 2 == 0:
                even.append(elem)
    return even

You can test this function with the provided assertion:

assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
"""

from collections import deque
from collections import Counter
import sys

def extract_even(t):
    even = []
    for elem in t:
        if isinstance(elem, tuple):
            even.append(extract_even(elem))
        else:
            if elem % 2 == 0:
                even.append(elem)
    return even

def extract_even2(t):
    even = deque([])
    for elem in t:
        if isinstance(elem, tuple):
            even.append(extract_even2(elem))
        else:
            if elem % 2 == 0:
                even.append(elem)
    return even

def extract_even3(t):
    even = []
    for elem in t:
        if isinstance(elem, tuple):
            even.append(extract_even3(elem))
        else:
            if elem % 2 == 0:
                even.append(elem)
    return even

def extract_even4(t):
    even = deque([])
    for elem in reversed(t):
        if isinstance(elem, tuple):
            even.