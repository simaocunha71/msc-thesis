def find_min_diff(nums: list,n: int) -> int:
  nums.sort()
  return min(nums[i+n] - nums[i] for i in range(len(nums)-n))