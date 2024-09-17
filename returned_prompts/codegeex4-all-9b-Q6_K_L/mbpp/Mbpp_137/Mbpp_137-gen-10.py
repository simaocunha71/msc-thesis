def zero_count(nums):
  num_zero = nums.count(0)
  num_non_zero = len(nums) - num_zero
  return num_zero / num_non_zero

