def max_Product(nums: list):
    nums.sort()
    return (nums[-1], nums[-2]) if nums[-1] * nums[-2] > nums[-1] * nums[-3] else (nums[-2], nums[-3])