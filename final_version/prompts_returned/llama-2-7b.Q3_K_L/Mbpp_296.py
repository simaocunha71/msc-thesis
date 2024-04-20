"""
Write a python function to count inversions in an array.
assert get_Inv_Count([1,20,6,4,5]) == 5
"""
class Solution:
    def findNumbers(self, nums):
        res = []
        
        while len(nums) > 0:
            if nums[0]>0:
                res.append(True)
                
            else:
                res.append(False)
            
            nums.pop()
        
        return res
    