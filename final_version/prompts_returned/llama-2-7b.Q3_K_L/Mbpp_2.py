"""
Write a function to find the shared elements from the given two lists.
assert set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))) == set((4, 5))
"""
class Solution:
    def __init__(self):
        self.dict = {}

    def remove_duplicates(self, nums):
        """Inserts all the element into dictionary."""
        if not nums or len(nums) == 0: return []
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        for j in nums:
            for k, v in self.dict.items():
                if j in v:
                    del self.dict[k][j]
            self.dict[j] = []
            
        for i, value in enumerate(nums):
            self.dict[value].append(i)
        return [str(num) for num, value in sorted(self.dict.items(), key=lambda x: len(x[1]))]
        
    def similar_elements(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: Set[int]
        """
        self.remove_duplicates(nums1)  # get rid of duplicate elements in nums1
        self.remove_duplicates(nums2)  # get rid of duplicate elements in nums2        
        ret = set()
        for i, v in enumerate(set(self.remove_duplicates(nums1))):
            for j, w in enumerate(self.remove_duplicates(nums2)):
                if v==w:
                    ret.add(i)  # only one unique number
        return list(ret)
                    