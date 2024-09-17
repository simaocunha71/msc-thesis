def sum_series(n: int) -> int:
  total = 0
  for i in range(n//2):
    total += (n-(2*i))
  return total