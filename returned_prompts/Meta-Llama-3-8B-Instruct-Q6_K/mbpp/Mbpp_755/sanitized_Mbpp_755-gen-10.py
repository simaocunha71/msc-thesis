def second_smallest(nums):
    nums.sort()
    return nums[1] if len(set(nums)) > 1 else None