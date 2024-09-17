def check_greater(nums: list, n: int) -> bool:
  for i in nums:
    if n < i:
      return True
  return False