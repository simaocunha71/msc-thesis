
def mul_even_odd(nums: list) -> int:
  even = 0
  odd = 0
  for i in nums:
    if i % 2 == 0:
      even = i
    else:
      odd = i
  return even * odd


