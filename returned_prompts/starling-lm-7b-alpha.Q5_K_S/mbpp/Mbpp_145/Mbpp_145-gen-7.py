
def max_Abs_Diff(nums:list) -> int:
  max_diff = 0
  for i in range(len(nums)-1):
    for j in range(i+1, len(nums)):
      max_diff = max(max_diff, abs(nums[i] - nums[j]))
  return max_diff


