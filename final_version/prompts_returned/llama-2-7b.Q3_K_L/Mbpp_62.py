"""
Write a python function to find smallest number in a list.
assert smallest_num([10, 20, 1, 45, 99]) == 1
"""
class Solution:
    def __init__(self):
        self.min = sys.maxsize
        
    
    def findSmallest(self, nums):
        for i in range (len(nums)):
            if len(nums) == 1 or self.min > nums[i]:
                self.min = nums[i]
                
            
        return self.min