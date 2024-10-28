def max_Product(nums):
    nums = sorted(nums, reverse=True)
    return nums[0], nums[1] if nums[1] != 0 else max((x for x in nums if x != 0), default=None)  # default=None is for the case where all numbers are 0