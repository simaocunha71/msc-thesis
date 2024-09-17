def pos_count(nums:list) -> int:
  count = 0
  for i in nums:
    if i > 0:
      count += 1
  return count