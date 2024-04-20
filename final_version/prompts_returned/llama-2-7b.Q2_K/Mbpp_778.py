"""
Write a function to pack consecutive duplicates of a given list elements into sublists.
assert pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])==[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
"""
class Solution:
    def packConsecutiveDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
    	if len(nums) == 0: return [[]]
        cur_n = 1 if nums[0] == 0 else 0 # the first element in list is 0
        ans_lst = []
        
        def helper(current, cur_n):
            while current < len(nums) and cur_n + nums[curent] <= cur_n:
                cur_n += nums[current+1]
                current+=2
            
            if cur_n == 0:
                ans_lst.append([])
            else:
                helper(current, cur_n)
        helper(0, cur_n)
        
        return ans_lst