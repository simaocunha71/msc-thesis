def sum_series(n):
  sum = 0
  while n > 0:
    sum += n
    n -= 2
  return sum