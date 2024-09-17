import math
def even_binomial_Coeff_Sum(n):
  sum = 0
  for i in range(0, n+1, 2):
    sum += math.comb(n, i)
  return sum