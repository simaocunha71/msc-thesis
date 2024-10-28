def cummulative_sum(nums: list) -> int:
  total = 0
  for tup in nums:
    total += sum(tup)
  return total

