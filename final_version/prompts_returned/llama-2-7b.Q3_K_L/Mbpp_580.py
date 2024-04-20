"""
Write a function to remove uneven elements in the nested mixed tuple.
assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
"""
from typing import Tuple

def extract_even(t:Tuple[float, *]) -> Tuple[float, ...]:
    """
    :type t: Tuple[float, *]
    :rtype: Tuple[float, ...]
    """
    result = []
    if len(t) == 1:
        return t[0],
    else:
        t2 = t[::2]
        for i in range(len(t)):
            if (i + 1) % 2 != 0:
                t2.append(t[i])
                result.append(t[i])
        return tuple(result)