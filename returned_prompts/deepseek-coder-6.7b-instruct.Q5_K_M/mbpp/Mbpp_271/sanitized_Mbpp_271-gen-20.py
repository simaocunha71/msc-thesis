def even_Power_Sum(n):
  total = 0
  for i in range(2, n*2+1, 2):
    total += i**5
  return total