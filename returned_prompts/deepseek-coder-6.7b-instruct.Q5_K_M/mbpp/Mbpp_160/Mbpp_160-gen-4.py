
def find_solution(a, b, n):
  if a == 0 and b == 0:
    return None
  if a == 0:
    if n % b == 0:
      return (0, n // b)
    else:
      return None
  if b == 0:
    if n % a == 0:
      return (n // a, 0)
    else:
      return None
  r, x = divmod(n, a)
  if x == 0:
    return (0, r)
  if b % a == 0:
    return (n // a - r, r)
  return None


