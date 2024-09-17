def is_octagonal(n):
  a = int((2*n+1)**0.5)
  b = int((2*n-1)**0.5)
  if a**2 + b**2 == 2*n:
    return a
  elif b**2 + a**2 == 2*n:
    return b