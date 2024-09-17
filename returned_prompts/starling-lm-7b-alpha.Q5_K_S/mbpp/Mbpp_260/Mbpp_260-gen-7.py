
def newman_prime(n):
  a = 2
  while True:
    a = (a*a + 1) % 1000000007
    if n == 0:
      return a
    n -= 1


