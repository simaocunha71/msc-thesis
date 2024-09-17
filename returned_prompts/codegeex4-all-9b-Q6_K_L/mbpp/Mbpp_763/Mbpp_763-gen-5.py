def find_min_diff(nums, n):
  nums.sort()
  min_diff = float('inf')
  for i in range(n-1):
    min_diff = min(min_diff, nums[i+1] - nums[i])
  return min_diff

