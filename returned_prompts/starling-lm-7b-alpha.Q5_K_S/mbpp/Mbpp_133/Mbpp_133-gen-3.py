
def sum_negativenum(nums: list) -> int:
  sum_negative = sum(num for num in nums if num < 0)
  return sum_negative


