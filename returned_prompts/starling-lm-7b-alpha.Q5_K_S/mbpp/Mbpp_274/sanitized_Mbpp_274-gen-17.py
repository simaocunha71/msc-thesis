def even_binomial_Coeff_Sum(n: int) -> int:
  coeff_sum = 0
  for i in range(n+1):
    if i%2==0:
      coeff_sum += 1
  return coeff_sum