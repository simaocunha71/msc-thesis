def sum_Of_product(n):
  total_sum = 0
  for i in range(1, n+1):
    binomial_coefficient = 1
    for j in range(1, i+1):
      binomial_coefficient *= (n-j+1) / j
    total_sum += binomial_coefficient
  return total_sum