def big_sum(nums: list) -> int:
  return sum(nums) - min(nums) - max(nums)