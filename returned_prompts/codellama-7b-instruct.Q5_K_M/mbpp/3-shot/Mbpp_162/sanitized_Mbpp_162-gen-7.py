def sum_series(n):
  sum = 0
  for i in range(int(n/2)):
    sum += n - (2*i)
  return sum