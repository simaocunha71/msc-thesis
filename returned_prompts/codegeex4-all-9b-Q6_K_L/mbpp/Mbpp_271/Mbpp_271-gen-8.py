def even_Power_Sum(n):
  sum = 0
  for i in range(2, 2*n, 2):
    sum += i**5
  return sum
