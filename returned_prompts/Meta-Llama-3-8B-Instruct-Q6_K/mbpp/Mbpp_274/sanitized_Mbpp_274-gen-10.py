def even_binomial_Coeff_Sum(n):
  sum_val = 0
  for i in range(n):
    if i % 2 == 0:
      sum_val += math.comb(n, i)
  return sum_val