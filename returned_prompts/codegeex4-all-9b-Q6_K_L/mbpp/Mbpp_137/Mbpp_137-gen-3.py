def zero_count(nums: list) -> float:
  zero_count = nums.count(0)
  total_count = len(nums)
  ratio = zero_count / total_count
  return ratio

