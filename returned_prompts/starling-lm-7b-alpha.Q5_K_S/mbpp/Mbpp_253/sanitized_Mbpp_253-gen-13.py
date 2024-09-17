def count_integer(nums: list) -> int:
  count = 0
  for n in nums:
    if isinstance(n, int):
      count += 1
  return count