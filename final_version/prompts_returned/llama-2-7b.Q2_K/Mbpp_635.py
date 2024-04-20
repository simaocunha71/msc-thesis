"""
Write a function to sort the given list.
assert heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
class Solution(object):
    def sortList(self, nums):
        """
        :type nums: List[int]
        :rtype: None
        """  
        if len(nums) == 0 or len(nums) ==1: return []
        
        def helper(i, j):
            if i > j:
                tmp = nums[:j+1]
                nums[:] += nums[j:-1] + nums[-2:]
                nums[0] -= 97 * len(tmp)
                return helper(i,j-1)
            else:
                tmp = nums[:i+1]
                nums[:] += nums[i:-1] + nums[-2:]
                nums[0] -= 97 * len(tmp)
                return helper(i+1, j)
        return helper(-1, len(nums))      
        pass