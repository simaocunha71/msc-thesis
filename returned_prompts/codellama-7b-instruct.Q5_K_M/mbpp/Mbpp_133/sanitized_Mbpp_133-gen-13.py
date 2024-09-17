def sum_negativenum(nums: list) -> int:
  return sum(filter(lambda x: x < 0, nums))