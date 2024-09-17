def zero_count(nums: list) -> float:
  num_zeroes = nums.count(0)
  num_non_zeroes = len(nums) - num_zeroes
  ratio = num_zeroes / num_non_zeroes
  return ratio

