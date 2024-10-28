
def sum_Of_product(n: int) -> int:
  return sum(binomial_coefficient(n, i) * binomial_coefficient(n, i+1) for i in range(n+1))

def binomial_coefficient(n: int, k: int) -> int:
  if k > n or k < 0:
    return 0
  if k == 0 or k == n:
    return 1
  return binomial_coefficient(n-1, k-1) + binomial_coefficient(n-1, k)


