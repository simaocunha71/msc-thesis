def find_solution(a, b, n):
  if n % gcd(a, b) != 0:
    return None
  x0 = 1
  y0 = 0
  x1 = 0
  y1 = 1
  while b > 0:
    q = a // b
    r = a % b
    a = b
    b = r
    x = x1 - q * x0
    y = y1 - q * y0
    x0 = x1
    y0 = y1
    x1 = x
    y1 = y
  return (x0 * n // a, y0 * n // a)
def gcd(a, b):
  while b != 0:
    a, b = b, a % b
  return a