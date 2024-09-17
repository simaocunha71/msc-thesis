def round_and_sum(nums:list) -> int:
  total = 0
  for i in nums:
    total += round(i)
  return total * len(nums)