def even_binomial_Coeff_Sum(n: int) -> int:
  if n == 0:
    return 0
  binomial_coeff = 1
  for i in range(2, n+1):
    if i % 2 == 0:
      binomial_coeff += 1
  return binomial_coeff