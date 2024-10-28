def is_polite(n: int) -> int:
  if n == 1:
    return 1
  elif n % 2 == 0:
    return is_polite(n//2) + 1
  else:
    return is_polite((n+1)//2) + 1