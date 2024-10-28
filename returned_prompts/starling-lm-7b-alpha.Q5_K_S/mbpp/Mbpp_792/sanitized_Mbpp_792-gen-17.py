def count_list(nums:list) -> int:
  count = 0
  for i in nums:
    if isinstance(i, list):
      count += 1
  return count