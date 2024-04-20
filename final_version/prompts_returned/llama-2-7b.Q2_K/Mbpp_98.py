"""
Write a function to multiply all the numbers in a list and divide with the length of the list.
assert math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001)
"""
import math
from typing import List
def multiply_num(nums:List):
    """
    :param nums: a list of numbers as tuples with at least one tuple and no more than 50
    :return: the result of multiplying all the numbers in the given list by their index into that list, then divided by the length of the list.
    """
    product=1.
    for i,(x,y) in enumerate(nums, start = 1):
        product *= x if math.isclose(x,y, abs_tol=0.001) else 1
    return math.floordiv(product, len(nums))
