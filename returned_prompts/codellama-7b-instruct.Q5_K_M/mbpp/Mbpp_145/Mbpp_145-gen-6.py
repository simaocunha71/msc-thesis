
def max_Abs_Diff(nums):
  max_diff = 0
  for i in range(len(nums)):
    for j in range(i+1, len(nums)):
      if abs(nums[i] - nums[j]) > max_diff:
        max_diff = abs(nums[i] - nums[j])
  return max_diff


