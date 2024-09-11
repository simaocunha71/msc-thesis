def find_min_diff(nums, k):
    nums.sort()
    res = float("inf")
    for i in range(len(nums) - k + 1):
        res = min(res, nums[i + k - 1] - nums[i])
    return res