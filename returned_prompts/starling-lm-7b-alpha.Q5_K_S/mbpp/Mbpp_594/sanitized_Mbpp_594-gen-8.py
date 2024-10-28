from typing import List
def diff_even_odd(nums: List[int]) -> int:
    i = 0
    while i < len(nums):
        if nums[i] % 2 == 0:
            break
        i += 1
    j = 0
    while j < len(nums):
        if nums[j] % 2 == 1:
            break
        j += 1
    return nums[j] - nums[i]