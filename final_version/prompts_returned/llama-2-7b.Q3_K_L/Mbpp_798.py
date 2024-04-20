"""
Write a python function to find the sum of an array.
assert _sum([1, 2, 3]) == 6
"""
class Solution:
    def _sum(self, nums):
        res = 0
        for num in nums:
            if not isinstance(num, int):
                return
            res += num

        return res