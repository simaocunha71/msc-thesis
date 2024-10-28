from math import comb
def bell_number(n):
  if n == 0:
    return 1
  else:
    return sum(comb(n, k) for k in range(n+1))