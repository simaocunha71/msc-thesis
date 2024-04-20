"""
Write a function to check if each element of second tuple is smaller than its corresponding element in the first tuple.
assert check_smaller((1, 2, 3), (2, 3, 4)) == False
"""
from typing import Tuple

def check_smaller(tuple1: Tuple[int], tuple2: Tuple[int]):
    """
    :type tuple1 Tuple[int]
    :param tuple1: the first tuple
    :type tuple2 Tuple[int]
    :param tuple2: the second tuple
    :return: True if every element in the second tuple is smaller than its corresponding elements in the first tuple
            otherwise return False.
    """
    for i, x in enumerate(tuple1):
        if not (x <= tuple2[i]):
            return False
    return True