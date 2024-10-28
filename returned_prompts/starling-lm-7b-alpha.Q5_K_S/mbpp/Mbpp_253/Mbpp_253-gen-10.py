
def count_integer(nums:list) -> int:
  count = 0
  for num in nums:
    if isinstance(num, int):
      count += 1
  return count


