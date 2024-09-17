def pos_count(nums: list) -> int:
  return sum(1 for n in nums if n > 0)