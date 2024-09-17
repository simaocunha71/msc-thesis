def find_lucas(n: int) -> int:
  if n == 1:
    return 2
  elif n == 2:
    return 1
  else:
    return find_lucas(n-1)+find_lucas(n-2)