"""
Write a python function to check if the elements of a given list are unique or not.
assert all_unique([1,2,3]) == True
"""
class Solution:
    def isUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cnt = {}
        for i in nums:
            if i not in cnt:
                cnt[i] = 1
            else:
                cnt[i] += 1
            
        return len(set(cnt.values())) == len(cnt)
