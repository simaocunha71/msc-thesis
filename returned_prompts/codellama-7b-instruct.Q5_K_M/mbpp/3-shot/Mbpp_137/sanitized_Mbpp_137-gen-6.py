def zero_count(nums: list) -> float:
  count = 0
  for num in nums:
    if num == 0:
      count += 1
  return count / len(nums)