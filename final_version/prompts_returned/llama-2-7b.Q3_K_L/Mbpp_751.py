"""
Write a function to check if the given array represents min heap or not. 
assert check_min_heap([1, 2, 3, 4, 5, 6]) == True
"""
class Solution(object):
    def isMinHeap(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
    	# write your code here
        if (len(nums) == 1 and not nums[-1] < nums[-2]):
            return False
            
        elif len(nums) > 2:
            for i in range(0, len(nums)-1): # to find out whether element at index i is less than element at index i+1.
                if not nums[i] < nums[i+1]:
                    return False
        else:
            pass