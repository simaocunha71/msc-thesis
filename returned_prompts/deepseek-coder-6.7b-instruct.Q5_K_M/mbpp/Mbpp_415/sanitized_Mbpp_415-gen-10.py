def max_Product(nums):
    nums.sort()
    if nums[0] < 0 and nums[1] < 0:
        return (nums[0], nums[1]) if nums[0] * nums[1] > nums[-1] * nums[-2] else (nums[-1], nums[-2])
    else:
        return (nums[-1], nums[-2])