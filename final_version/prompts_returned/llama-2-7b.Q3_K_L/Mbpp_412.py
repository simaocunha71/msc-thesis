"""
Write a python function to remove odd numbers from a given list.
assert remove_odd([1,2,3]) == [2]
"""
class Solution:
    def removeOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        
        if len(nums) <= 1: # if length is less then return it directly
            return list(nums)
        
        for i in range(0,len(nums)):
            odd = nums.count(i) > 1
            
            
            if odd == True:
                nums.remove(i)
                continue # so that we don't count it again
            
            print('if',odd,'in',i,', then break')
        return list(set(nums))