def mul_even_odd(nums: list) -> int:
  even = 1
  odd = 1
  for i in nums:
    if i % 2 == 0:
      even = even * i
    else:
      odd = odd * i
  return even * odd