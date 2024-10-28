def is_woodall(n: int) -> bool:
  sum = 0
  for i in range(1, n+1):
    sum += i**(i-1)
  return sum == n