def second_smallest(nums):
    if len(nums) < 2:
        return None
    nums.sort()
    return nums[1] if nums[1] != nums[0] else None