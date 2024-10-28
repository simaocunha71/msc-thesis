
def zero_count(nums: list) -> float:
  zero_nums = len([x for x in nums if x == 0])
  non_zero_nums = len(nums) - zero_nums
  return zero_nums / non_zero_nums


