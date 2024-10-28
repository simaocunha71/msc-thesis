
def zero_count(nums: list) -> float:
  zero_count = 0
  for num in nums:
    if num == 0:
      zero_count += 1
  return zero_count / len(nums)


