def sum_Of_product(n: int) -> int:
  sum = 0
  for i in range(1, n):
    sum += (math.factorial(n) / (math.factorial(i) * math.factorial(n - i))) * (math.factorial(n) / (math.factorial(i) * math.factorial(n - i)))
  return sum

