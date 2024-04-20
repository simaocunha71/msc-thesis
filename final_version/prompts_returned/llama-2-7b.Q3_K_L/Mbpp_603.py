"""
Write a function to get all lucid numbers smaller than or equal to a given integer.
assert get_ludic(10) == [1, 2, 3, 5, 7]
"""
from typing import List

def get_lucid(max:int)->List[int]:
    """Returns all ludic numbers smaller than a given max.
    1 lucid number is the smallest integer n such that n^2 == n + 1 (n=4 in this case)
    
    https://www.mathsisfun.com/lucas-numbers.html
    """
    lucids = [0]*max+1
    for i in range(2, max+1):
        if i*i == i + 1:
            lucids[i] = i
    
    return lucids

# Tests
assert get_lucid(3) == [4,5]
assert get_lucid(7) == [0,1,2,3,4,5,6,7]