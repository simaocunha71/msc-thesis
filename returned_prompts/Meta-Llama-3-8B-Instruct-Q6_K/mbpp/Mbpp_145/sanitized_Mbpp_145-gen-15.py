def max_Abs_Diff(arr):
    if len(arr) < 2:
        return 0
    nums = [x for x in arr if isinstance(x, (int, float))]
    if len(nums) < 2:
        return 0
    return max(nums) - min(nums)