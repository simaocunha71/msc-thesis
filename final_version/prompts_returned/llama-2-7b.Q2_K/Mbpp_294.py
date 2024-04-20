"""
Write a function to find the maximum value in a given heterogeneous list.
assert max_val(['Python', 3, 2, 4, 5, 'version'])==5
"""
class Solution:
    def findMax(self, nums):
        if type(nums) == int:   #if the input is an integer number
            return nums
            
        max_val = -float('inf')
        
        for val in nums:
            if (max_val < val):    #find max value
                max_val = val       #store max value, as it may be used multiple times
                    
        return max_val
        