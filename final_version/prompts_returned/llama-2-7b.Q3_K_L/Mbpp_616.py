"""
Write a function which takes two tuples of the same length and performs the element wise modulo.
assert tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5)) == (0, 4, 5, 1)
"""
from typing import *

def tuple_modulo(t1: Tuple, t2: Tuple):
    """
    Write a function which takes two tuples of the same length and performs the element wise modulo.
    assert tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5)) == (0, 4, 5, 1)
    """
    def tuple_mod(x: Tuple, y: Tuple):
        result = []
        for i in range(len(x)):
            result.append(i % len(y))
        return result
    mod = tuple_mod(t1, t2)
    return mod
