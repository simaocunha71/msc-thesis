def find_min_diff(nums: list, n: int) -> int:
  nums.sort()
  return min(nums[i] - nums[i-1] for i in range(1, n))

