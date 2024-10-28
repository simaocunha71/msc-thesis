def max_Product(nums):
    if len(nums) < 2:
        return None
    nums.sort()
    if nums[-1] > 0:
        return (nums[-1], nums[-2])
    else:
        return (nums[0], nums[1]) if nums[0] < 0 else (nums[-1], nums[-2])  # handle negative numbers