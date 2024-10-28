
def sum_series(n):
  total = 0
  i = 0
  while n - 2 * i >= 0:
    total += n - 2 * i
    i += 1
  return total


