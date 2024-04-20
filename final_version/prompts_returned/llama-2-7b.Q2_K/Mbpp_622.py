"""
Write a function to find the median of two sorted lists of same size.
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
"""
class Solution:
    def getMedian(self, nums1: List[int], nums2: List[int], target : int) -> float:
        if len(nums1 + nums2) != target + 1:
            return self.getMedian(nums1, [])
        
        total = sum([i for i in nums1 + nums2])
        middleIndex = (target - 1) // 2
        if total % 2 == 0 and total >= target :
            middleIndex += 1
        return (total-1)/2.0 + self.getMedian([], [])
        