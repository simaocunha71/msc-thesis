
def zero_count(nums: list) -> float:
  zero_count = len([i for i in nums if i==0])
  return zero_count / len(nums)


