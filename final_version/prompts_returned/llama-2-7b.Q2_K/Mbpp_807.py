"""
Write a python function to find the first odd number in a given list of numbers.
assert first_odd([1,3,5]) == 1
"""

def first_odd(nums):
    if len(nums) < 1:
        return None
    
    for idx, num in enumerate(nums[0]):
        if odd(idx, num):
            break
        
    else:
        return None
            
    return idx

def odd(num_1, num):
    return (num % 2) != 0