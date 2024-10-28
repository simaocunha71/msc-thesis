
def sum_negativenum(nums: list) -> int:
  sum_num = 0
  for i in nums:
    if i < 0:
      sum_num += i
  return sum_num


