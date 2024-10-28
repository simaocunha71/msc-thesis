
def first_odd(nums: list) -> int:
  for num in nums:
    if num % 2 == 1:
      return num
  return None


