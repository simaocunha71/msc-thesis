"""
Write a function to find kth element from the given two sorted arrays.
assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
"""
class Solution:
    def findKthNumber(self, nums: List[int], k: int) -> int:
        n = len(nums) + 1
        res = []

        for i in range(n):
            num = -1 if i < k else i
            res.append((k-i+1, num))
        return max([i[0] if (k > 2*i[1]+1) else i for i in res])[1]
