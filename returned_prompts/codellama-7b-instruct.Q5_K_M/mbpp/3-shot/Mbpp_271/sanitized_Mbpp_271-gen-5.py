def even_Power_Sum(n):
  total = 0
  for num in range(2, n+1):
    if num % 2 == 0:
      total += num ** 5
  return total