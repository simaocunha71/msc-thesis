
def frequency(nums:list, n: int) -> int:
  count = 0
  for i in nums:
    if i == n:
      count += 1
  return count


