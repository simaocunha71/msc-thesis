
def is_polite(n: int) -> int:
  if n == 1:
    return 2
  elif n % 2 == 0:
    return is_polite(n-1) + 1
  else:
    return is_polite(n-1) + 9


