def count_list(nums: list) -> int:
  count = 0
  for num in nums:
    if isinstance(num, list):
      count += 1
  return count