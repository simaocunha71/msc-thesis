"""
Write a python function to check whether any value in a sequence exists in a sequence or not.
assert overlapping([1,2,3,4,5],[6,7,8,9]) == False
"""
class Solution:
    def overlapping(self, nums1: List[int], nums2: List[int]) -> bool:
        if len(nums1) < len(nums2):
            return self.overlapping(nums1 + [i] * (len(nums2)-len(nums1)), 
                                     nums2)
        
        for i in range(len(nums1)):
            if nums1[i] == nums2[i]:
                return True