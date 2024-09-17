def count_integer(nums):
  count = 0
  for i in nums:
    if isinstance(i, int):
      count += 1
  return count

