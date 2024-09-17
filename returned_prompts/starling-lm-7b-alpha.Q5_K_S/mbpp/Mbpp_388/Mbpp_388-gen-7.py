
def highest_Power_of_2(n: int) -> int:
  p = 0
  while (2**p) <= n:
    p += 1
  return 2**(p-1)


