"""
Write a function to count the number of occurrences of a number in a given list.
assert frequency([1,2,3], 4) == 0
"""
class Solution:
    def frequency(self, nums: List[int]) -> int:
        res = [0] * len(nums)

        for i, n in enumerate(nums):
            if n < 0:
                res[n + len(nums)] -= 1
            else:
                res[n] += 1
            
        return sum(res[:])
