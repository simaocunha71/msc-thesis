def zero_count(nums: list) -> float:
  zero_nums = sum([1 for i in nums if i == 0])
  total_nums = len(nums)
  return zero_nums / total_nums