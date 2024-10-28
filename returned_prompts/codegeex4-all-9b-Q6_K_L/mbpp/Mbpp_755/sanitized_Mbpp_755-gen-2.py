def second_smallest(nums):
    nums = list(set(nums))
    if len(nums) < 2:
        return None
    nums.sort()
    return nums[1]