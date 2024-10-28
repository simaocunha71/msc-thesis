def frequency(nums: list,n: int) -> int:
  count = 0
  for num in nums:
    if num == n:
      count += 1
  return count