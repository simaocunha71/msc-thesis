def second_smallest(nums):
    nums = list(set(nums))
    nums.sort()
    if len(nums) < 2:
        return None
    return nums[1] if nums[0] != nums[1] else None