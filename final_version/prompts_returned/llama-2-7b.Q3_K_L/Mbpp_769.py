"""
Write a python function to get the difference between two lists.
assert (Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) == [10, 20, 30, 15]
"""
class Solution(object):
    def Diff(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        
        if len(nums1) != len(nums2) or not isinstance (nums1, list): return []
        res = []
        for i in range(len(nums1)):
            res.append(abs((nums1[i] - nums2[i])) ) 
        
    # print(res)
    
    def __repr__(self):
        return f"{self.__class__.__name__}()"
    if __name__ == "__main__":
        s = Solution()
        assert (Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) == [10, 20, 30, 15]