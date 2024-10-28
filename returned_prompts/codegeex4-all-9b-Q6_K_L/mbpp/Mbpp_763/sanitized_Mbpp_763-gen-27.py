def find_min_diff(nums: list, n: int) -> int:
  nums.sort()
  min_diff = float('inf')
  for i in range(n - 1):
      diff = nums[i + 1] - nums[i]
      if diff < min_diff:
          min_diff = diff
  return min_diff