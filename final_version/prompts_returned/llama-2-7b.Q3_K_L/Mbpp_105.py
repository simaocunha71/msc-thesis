"""
Write a python function to count true booleans in the given list.
assert count([True,False,True]) == 2
"""
class Solution:
    def count(self, nums):
        if not isinstance(nums, (list, tuple)):
            return 0
        
        res = Counter()
        for element in nums:
            res[element] += 1
        return sum([res.get(x) for x in res])
