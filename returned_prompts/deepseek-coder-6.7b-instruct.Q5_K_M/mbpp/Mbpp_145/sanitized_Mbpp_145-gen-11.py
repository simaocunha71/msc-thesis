def max_Abs_Diff(nums):
  return max(abs(a - b) for a, b in zip(nums, nums[1:]))