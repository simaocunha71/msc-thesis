def find_solution(a, b, n):
  if a == 0 and b == 0:
    return None
  if a == 0:
    return (0, n // b) if n % b == 0 else None
  if b == 0:
    return (n // a, 0) if n % a == 0 else None
  r, x, y = 1, 0, 0
  while r != 0:
    q = n // a
    r = n % a
    n, a = a, r
    x, y = y - q * x, x
  return (n, y) if n == 1 else (y, x)