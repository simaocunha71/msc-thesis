
def next_Perfect_Square(n):
  if n < 0:
    return -1
  while True:
    n += 1
    if n**2 > 10000:
      return -1
    if n**2 % 4 == 0:
      return n**2


