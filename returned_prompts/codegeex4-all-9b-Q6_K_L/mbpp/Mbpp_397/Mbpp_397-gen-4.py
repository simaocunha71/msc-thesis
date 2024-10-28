def median_numbers(a, b, c):
    nums = sorted([a, b, c])
    return nums[1] if len(nums) % 2 == 1 else (nums[0] + nums[1]) / 2.0