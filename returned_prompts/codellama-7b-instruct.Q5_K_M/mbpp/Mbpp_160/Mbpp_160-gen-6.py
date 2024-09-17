
def find_solution(a, b, n):
  gcd, x, y = ext_gcd(a, b)
  if gcd == n:
    return x, y
  if gcd % n == 0:
    return x % n, y % n
  return None

def ext_gcd(a, b):
  if a == 0:
    return b, 0, 1
  else:
    gcd, y, x = ext_gcd(b % a, a)
    return gcd, x - (b // a) * y, y


