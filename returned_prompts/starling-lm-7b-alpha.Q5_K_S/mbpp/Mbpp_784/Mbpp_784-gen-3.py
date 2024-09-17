
def mul_even_odd(nums: list) -> int:
  even = [i for i in nums if i % 2 == 0]
  odd = [i for i in nums if i % 2 != 0]
  if len(even) == 0:
    return 0
  elif len(odd) == 0:
    return even[0]
  else:
    return even[0] * odd[0]


