def sumofFactors(n):
  sum_even_factors = 0
  for i in range(1, n + 1):
    if i % 2 == 0 and n % i == 0:
      sum_even_factors += i
  return sum_even_factors