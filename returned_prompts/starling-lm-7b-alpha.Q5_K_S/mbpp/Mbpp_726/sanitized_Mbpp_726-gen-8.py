import numpy as np
from itertools import starmap
def multiply_elements(t):
    """
    >>> multiply_elements((1, 5, 7, 8, 10))
    (5, 35, 56, 80)
    """
    res = []
    for i in range(len(t)-1):
        res.append(t[i]*t[i+1])
    return tuple(res)