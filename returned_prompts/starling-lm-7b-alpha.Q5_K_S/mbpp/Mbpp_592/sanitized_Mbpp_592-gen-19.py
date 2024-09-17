def sum_Of_product(n: int):
  return sum(i*(n-i) for i in range(n+1))