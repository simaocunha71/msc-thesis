"""
Write a python function to find smallest number in a list.
assert smallest_num([10, 20, 1, 45, 99]) == 1
"""

def smallest(nums):
    if not nums:
        return 'No Numbers'
    
    else:
       min_num = (min(nums))
  
       return str(min_num)