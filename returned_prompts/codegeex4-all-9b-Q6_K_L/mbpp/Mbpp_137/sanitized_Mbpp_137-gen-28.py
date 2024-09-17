def zero_count(nums: list) -> float:
  zero_count = nums.count(0)
  total_nums = len(nums)
  ratio = zero_count / total_nums
  return ratio