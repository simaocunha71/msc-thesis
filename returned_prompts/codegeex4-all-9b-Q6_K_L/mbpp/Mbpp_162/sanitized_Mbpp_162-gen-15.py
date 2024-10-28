def sum_series(n):
  if n == 1:
    return 1
  return n + sum_series(n-2)