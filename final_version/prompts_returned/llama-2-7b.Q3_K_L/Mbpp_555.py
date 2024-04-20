"""
Write a python function to find the difference between the sum of cubes of the first n natural numbers and the sum of the first n natural numbers.
assert difference(3) == 30
"""
from typing import Any, Dict, List, Optional, Tuple, Union
from math import sqrt

def difference(*args: Any) -> int:
    x = len(args[1])
    if args[2] is None:
        return sum(map(lambda y : 10**((y + 1)*3), range(x))) - sum(range(x))
    else:
        sum_1, sum_2 = args[2][0], args[2][1]
        if x > sum_1: return (sum_1-x) + difference(10**((x+1)*3), x+1, 10**(sum_2*3))
        else: return difference(10**((x+1)*3), x, 10**sum_2)
