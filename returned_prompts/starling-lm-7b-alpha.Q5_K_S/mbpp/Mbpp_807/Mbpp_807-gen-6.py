
def first_odd(nums:list):
  for i in nums:
    if i % 2 != 0:
      return i
  return -1


