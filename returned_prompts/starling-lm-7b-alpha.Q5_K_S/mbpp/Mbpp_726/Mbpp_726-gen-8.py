def multiply_elements(t):
    """
    >>> multiply_elements((1, 5, 7, 8, 10))
    (5, 35, 56, 80)
    """
    res = []
    for i in range(len(t)-1):
        res.append(t[i]*t[i+1])
    return tuple(res)

# Here is a more efficient version using list comprehension and slicing:
def multiply_elements_2(t):
    """
    >>> multiply_elements((1, 5, 7, 8, 10))
    (5, 35, 56, 80)
    """
    return tuple([t[i]*t[i+1] for i in range(len(t)-1)])

# Here is an even more efficient version using multiplication operator:
def multiply_elements_3(t):
    """
    >>> multiply_elements((1, 5, 7, 8, 10))
    (5, 35, 56, 80)
    """
    return tuple(a * b for a, b in zip(t[:-1], t[1:]))

# Here is an even more efficient version using slicing:
def multiply_elements_4(t):
    """
    >>> multiply_elements((1, 5, 7, 8, 10))
    (5, 35, 56, 80)
    """
    return tuple(t[:-1] * t[1:])

# Here is an even more efficient version using numpy:
import numpy as np
def multiply_elements_5(t):
    """
    >>> multiply_elements((1, 5, 7, 8, 10))
    (5, 35, 56, 80)
    """
    return tuple(np.multiply(t[:-1], t[1:]))

# Here is an even more efficient version using itertools:
from itertools import starmap
def multiply_elements_6(t):
    """
