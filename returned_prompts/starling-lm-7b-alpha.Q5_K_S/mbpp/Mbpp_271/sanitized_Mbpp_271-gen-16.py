def even_Power_Sum(n):
  total_sum = 0
  for i in range(1, n+1):
    total_sum += i**5
  return total_sum