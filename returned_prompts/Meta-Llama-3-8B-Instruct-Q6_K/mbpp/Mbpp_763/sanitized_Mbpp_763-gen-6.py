def find_min_diff(nums):
    nums = sorted(nums)
    min_diff = float('inf')
    for i in range(1, len(nums)):
        diff = nums[i] - nums[i-1]
        if diff < min_diff:
            min_diff = diff
    return min_diff