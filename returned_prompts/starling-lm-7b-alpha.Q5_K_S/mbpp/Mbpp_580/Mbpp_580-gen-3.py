"""
def extract_even(t):
    if isinstance(t, tuple):
        return (x for x in t if not isinstance(x, tuple) or extract_even(x) and x % 2 == 0)
    else:
        return t % 2 == 0

assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
"""

from typing import Tuple, Union, List

def extract_even(t: Tuple) -> Tuple:
    if isinstance(t, tuple):
        return (x for x in t if not isinstance(x, tuple) or extract_even(x) and x % 2 == 0)
    else:
        return t % 2 == 0

assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)

"""
def extract_even(t: Tuple) -> Tuple:
    result = []
    for elem in t:
        if isinstance(elem, tuple):
            if elem and not any(map(lambda x: isinstance(x, tuple), elem)):
                result.append(elem)
        else:
            if elem % 2 == 0:
                result.append(elem)
    return tuple(result)

assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
"""

"""
def extract_even(t: Tuple) -> Tuple:
    result = []
    for elem in t:
        if isinstance(elem, tuple):
            if elem and all(map(lambda x: not isinstance(x, tuple), elem)):
                result.append(elem)
        else:
            if elem % 2 == 0:
                result.append(elem)
    return tuple(result)

assert extract_even((4, 5, (