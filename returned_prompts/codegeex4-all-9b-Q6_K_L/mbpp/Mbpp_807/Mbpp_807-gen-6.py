def first_odd(nums):
  for i in nums:
    if i % 2 != 0:
      return i
  return None

