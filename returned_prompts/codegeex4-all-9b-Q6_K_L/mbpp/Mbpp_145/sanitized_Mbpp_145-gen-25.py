def max_Abs_Diff(nums):
    if len(nums) < 2:
        return 0
    max_diff = nums[1] - nums[0]
    min_num = nums[0]
    max_num = nums[1]
    for i in range(1, len(nums)):
        min_num = min(min_num, nums[i])
        max_num = max(max_num, nums[i])
        max_diff = max(max_diff, max_num - min_num)
    return max_diff