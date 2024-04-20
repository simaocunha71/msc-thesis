"""
Write a function to find the ratio of zeroes to non-zeroes in an array of integers.
assert math.isclose(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, rel_tol=0.001)
"""
import math
from typing import List

def zero_count(nums:List[int]) -> float :
    """
    Find the ratio of zeroes to non-zeroes in an array of integers. 
    Return a float of the ratio.
    
    Example:
        Input: [0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]
        
        Output:  0.181818
        
    
    """
    nums_len = len(nums)
    total = 0
    count = 0
    for i in range(nums_len-1):
        if (nums[i] == 0 or nums[i+1] == 0):
            total+=1
            
    return float(total)/float(count)