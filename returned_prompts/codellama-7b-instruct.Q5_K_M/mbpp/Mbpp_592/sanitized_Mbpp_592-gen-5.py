def sum_Of_product(n):
  return sum([binomial_coefficient(n, i) * binomial_coefficient(n, n - i) for i in range(n)])
def binomial_coefficient(n, k):
  if k == 0 or k == n:
    return 1
  return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)