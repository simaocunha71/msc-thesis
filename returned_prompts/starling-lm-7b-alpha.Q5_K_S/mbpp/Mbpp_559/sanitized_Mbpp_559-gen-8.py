from typing import List
def max_sub_array_sum(nums: List[int], k: int):
    n = len(nums)
    if n < k:
        return 0

    max_sum = float('-inf')
    for i in range(k):
        max_sum = max(max_sum, nums[i])

    for i in range(k, n):
        max_sum = max(max_sum + nums[i] - nums[i-k], nums[i])

    return max_sum