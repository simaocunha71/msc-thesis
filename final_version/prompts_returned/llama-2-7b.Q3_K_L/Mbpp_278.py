"""
Write a function to find the number of elements that occurs before the tuple element in the given tuple.
assert count_first_elements((1, 5, 7, (4, 6), 10) ) == 3
"""
from typing import Tuple

def count_first_elements(tuple:Tuple[int]) -> int :
    """
    Write a function that takes a tuple as the argument and returns the number of occurrences of each element in the tuple.
    The function should return an array with indices of the numbers present in the tuple given in the input, for example, if the tuple is (1, 5, 7) , it should return [0,2] where index '0' denotes the first occurrence and index '2' represents the second occurrence.
    """
    return sorted(list(set([x for x,y in enumerate(tuple)])))