def is_Monotonic(nums: list) -> bool:
    return all(x <= y for x, y in zip(nums, nums[1:])) or all(x >= y for x, y in zip(nums, nums[1:]))