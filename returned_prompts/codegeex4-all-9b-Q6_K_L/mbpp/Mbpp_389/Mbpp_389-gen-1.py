def find_lucas(n: int) -> int:
  if n == 0:
    return 2
  elif n == 1:
    return 1
  else:
    a, b = 2, 1
    for _ in range(n - 1):
      a, b = b, a + b
    return a

