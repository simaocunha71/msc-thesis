def max_Abs_Diff(nums):
    return max([abs(nums[i] - nums[i+1]) for i in range(len(nums)-1)])


