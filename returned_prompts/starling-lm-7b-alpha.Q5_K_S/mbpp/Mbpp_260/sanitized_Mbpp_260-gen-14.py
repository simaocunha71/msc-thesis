def newman_prime(n: int) -> int:
  a = 2
  c = 1
  b = 1
  while True:
    a, c, b = (2*a + b)%15, b, c
    if c == n:
      return a