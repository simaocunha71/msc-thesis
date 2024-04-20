"""
Write a function to find the median of three numbers.
assert median_numbers(25,55,65)==55.0
"""
from typing import List

def median_numbers(nums: List[int]):
    if len(nums) == 3:
        return nums[-1] + nums[-2]+ nums[-3]//3
    
    elif len(nums) > 3:
        middle=len(nums)/2-1;
        median_left=median_numbers(nums[:middle])
        median_right=median_numbers(nums[middle+1:])
        
        return (median_left + median_right)//2  