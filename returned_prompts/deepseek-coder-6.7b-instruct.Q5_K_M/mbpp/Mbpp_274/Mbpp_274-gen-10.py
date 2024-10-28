
def even_binomial_Coeff_Sum(n):
  binomial_coeff = [0 for _ in range(n+1)]
  binomial_coeff[0] = 1
  sum = 0
  for i in range(1, n+1):
    j = 0
    while(j<i):
      binomial_coeff[j] = binomial_coeff[j] + binomial_coeff[j+1]
      j += 1
  for i in range(n):
    if i % 2 == 0:
      sum += binomial_coeff[i]
  return sum

