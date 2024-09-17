def check_greater(nums: list,n: int) -> bool:
  for i in nums:
    if i > n:
      return True
  return False