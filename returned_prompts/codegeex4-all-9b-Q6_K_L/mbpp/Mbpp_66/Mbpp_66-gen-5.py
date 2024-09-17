def pos_count(nums: list) -> int:
  pos_count = sum(1 for num in nums if num > 0)
  return pos_count

