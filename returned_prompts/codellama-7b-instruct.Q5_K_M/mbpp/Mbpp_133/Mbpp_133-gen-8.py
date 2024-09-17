
def sum_negativenum(nums: list) -> int:
  sum = 0
  for i in nums:
    if i < 0:
      sum += i
  return sum


