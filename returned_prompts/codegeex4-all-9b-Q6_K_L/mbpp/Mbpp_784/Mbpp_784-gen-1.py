def mul_even_odd(lst):
  even = 1
  odd = 1
  for i in lst:
    if i % 2 == 0:
      even *= i
    else:
      odd *= i
  return even * odd


