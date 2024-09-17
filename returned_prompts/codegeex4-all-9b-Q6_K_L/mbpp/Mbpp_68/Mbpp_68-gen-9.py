def is_Monotonic(nums: list) -> bool:
    return nums == sorted(nums) or nums == sorted(nums, reverse=True)

