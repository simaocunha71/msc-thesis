def pos_count(nums: list) -> int:
  pos_count = 0
  for num in nums:
    if num > 0:
      pos_count += 1
  return pos_count