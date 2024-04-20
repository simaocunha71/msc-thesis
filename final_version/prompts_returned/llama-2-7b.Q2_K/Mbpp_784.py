"""
Write a function to find the product of first even and odd number of a given list.
assert mul_even_odd([1,3,5,7,4,1,6,8])==4
"""
from typing import Optional

def mul_even_odd(nums: list) -> int or None:
    """Return the product of first even and odd number in input list. Return None if len(nums) is not even"""
    if (len(nums) % 2 == 0):
        return None
    
    prod_1 = nums[0] * nums[1]
    prod_2 = None
    prod_3 = None
    for i in range(2, len(nums), 2):
      prod_2 = prod_1 * nums[i] if (prod_1 is not None) else prod_2
      prod_3 = prod_2 * nums[i+1] if (prod_2 is not None) else prod_3
      
    return prod_3 or prod_2 or prod_1
