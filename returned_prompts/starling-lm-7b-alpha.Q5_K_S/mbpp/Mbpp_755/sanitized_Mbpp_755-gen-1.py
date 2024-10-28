from typing import List
def second_smallest(nums: List[int]) -> int:
    nums.sort()
    return nums[1]