
def zero_count(nums):
  zero_count = nums.count(0)
  non_zero_count = len(nums) - zero_count
  return zero_count / non_zero_count


