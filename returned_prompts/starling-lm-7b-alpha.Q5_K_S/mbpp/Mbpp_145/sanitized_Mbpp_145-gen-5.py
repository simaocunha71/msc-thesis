def max_Abs_Diff(nums):
    if len(nums) < 2:
        return 0
    max_abs_diff = 0
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            max_abs_diff = max(max_abs_diff, abs(nums[i] - nums[j]))
    return max_abs_diff