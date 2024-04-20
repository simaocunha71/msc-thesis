"""
Write a python function to find the length of the smallest list in a list of lists.
assert Find_Min_Length([[1],[1,2]]) == 1
"""
class Solution:
    def find_min_length(self, nums):
        '''
        Time complexity = O(n)
        Space complexity=O(1) (one temp variable)
        
        '''
        if not nums: return 0
        else:
            minlen = len(nums[0])
            
            for x in nums:
                temp = len(x)
                
                if temp < minlen:
                    minlen = temp