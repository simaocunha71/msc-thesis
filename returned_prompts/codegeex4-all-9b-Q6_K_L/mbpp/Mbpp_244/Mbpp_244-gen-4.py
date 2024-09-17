def next_Perfect_Square(n):
  n = n + 1
  while True:
    if int(math.sqrt(n))**2 == n:
      return n
    n += 1

