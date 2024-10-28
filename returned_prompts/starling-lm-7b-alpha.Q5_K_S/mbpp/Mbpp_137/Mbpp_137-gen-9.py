
def zero_count(nums: list) -> float:
  zero_count = len([n for n in nums if n == 0])
  return zero_count / len(nums)


