def sum_Of_product(n):
  res = 0
  for i in range(1, n+1):
    res += math.factorial(n) / (math.factorial(i) * math.factorial(n-i))
  return res