"""
Write a function to find the list of maximum length in a list of lists.
assert max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(3, [13, 15, 17])
"""
class Solution:
    def findMaxLength(self, nums):
        if not isinstance(nums,(list)): raise TypeError("Argument must be a list")
        
        max_length=(0,[])
        min_length=len(nums)
        for i in range(min_length-1,-1,-1):
            if (max_length[0]+nums[i]>max_length or not isinstance(nums[i],list)):
                max_length=(max_length[0]+nums[i], [])+max_length
            else:
                max_length=max(max_length)
        return (max_length[1], max_length[2]+max_length[0]+min_length-len(max_length))