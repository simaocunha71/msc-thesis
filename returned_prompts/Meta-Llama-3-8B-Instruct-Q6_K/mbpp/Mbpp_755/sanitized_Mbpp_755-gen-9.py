def second_smallest(nums):
    if len(nums) < 2:
        raise ValueError("List must have at least two elements.")
    nums = sorted(set(nums))
    return nums[1] if len(nums) > 1 else None