def is_polite(n: int) -> bool:
  for i in range(1, n):
    if n % i == 0:
      return True
  return False