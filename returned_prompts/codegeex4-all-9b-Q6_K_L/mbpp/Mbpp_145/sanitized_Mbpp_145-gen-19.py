def max_Abs_Diff(nums: list) -> int:
    max_diff = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            diff = abs(nums[i] - nums[j])
            if diff > max_diff:
                max_diff = diff
    return max_diff