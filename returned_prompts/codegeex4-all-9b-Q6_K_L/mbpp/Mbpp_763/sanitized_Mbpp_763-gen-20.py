def find_min_diff(nums, n):
    nums.sort()
    return min(nums[i] - nums[i - 1] for i in range(1, n))