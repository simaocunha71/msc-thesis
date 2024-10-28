
def find_lucas(n: int) -> int:
  a = 2
  b = 1
  if n == 1:
    return b
  elif n == 2:
    return a
  else:
    for i in range(2,n+1):
      c = a + b
      a = b
      b = c
    return b


