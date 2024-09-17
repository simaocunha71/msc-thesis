def pos_count(nums:list) -> int:
  count = 0
  for num in nums:
    if num > 0:
      count += 1
  return count