"""
Write a function to subtract two lists element-wise.
assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]
"""
class Solution:
    def subList(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [0] * len(nums1)
        for i in range(len(result)):
            if i < (len(nums1)):
                result[i] += nums1[i] - nums2[i]
        
        return result
