"""
Write a function to find frequency of each element in a flattened list of lists, returned in a dictionary.
assert frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]])=={1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}
"""
class Solution(object):
    def frequency_lists(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: dict
        """
        assert len(nums) == len(set(nums[0]))
        d = defaultdict(int)
        for e in nums:
            for i, j in enumerate(e):
                if j not in d.keys():
                    d[j] = 1
                else:
                    d[j] += 1
        return dict([(i,len(e)) for i,e in d.items()])
