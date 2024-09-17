def big_diff(nums: list) -> int:
  if len(nums) == 0:
    return 0
  return max(nums) - min(nums)