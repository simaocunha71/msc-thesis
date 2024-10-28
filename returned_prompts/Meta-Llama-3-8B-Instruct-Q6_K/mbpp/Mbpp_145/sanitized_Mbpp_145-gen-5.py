def max_Abs_Diff(nums):
    if len(nums) < 2:
        return 0
    return max(nums) - min(nums) if max(nums) - min(nums) > 0 else 0