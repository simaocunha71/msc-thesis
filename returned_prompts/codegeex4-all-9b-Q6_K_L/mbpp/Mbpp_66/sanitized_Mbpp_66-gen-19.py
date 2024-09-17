def pos_count(nums: list) -> int:
  count = sum(1 for num in nums if num > 0)
  return count