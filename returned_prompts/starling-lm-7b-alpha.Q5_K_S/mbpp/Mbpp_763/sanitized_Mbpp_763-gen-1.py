from typing import List
def find_min_diff(nums: List[int], target: int) -> int:
    nums.sort()
    min_difference = float('inf')
    for i in range(len(nums)):
        if target == nums[i]:
            min_difference = 0
            break
        diff = target - nums[i]
        if diff < min_difference:
            min_difference = diff
    return min_difference