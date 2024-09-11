def second_smallest(nums):
    if len(nums) < 2:
        return None
    nums = sorted(set(nums))
    return nums[1] if len(nums) > 1 else None