def sum_Of_product(n: int) -> int:
  binomial_coefficients = [1]
  sum_of_product = 0
  for i in range(1, n+1):
    binomial_coefficients.append(binomial_coefficients[i-1] * (n-i+1)/i)
  for i in range(len(binomial_coefficients)-1):
    sum_of_product += binomial_coefficients[i] * binomial_coefficients[i+1]
  return int(sum_of_product)


