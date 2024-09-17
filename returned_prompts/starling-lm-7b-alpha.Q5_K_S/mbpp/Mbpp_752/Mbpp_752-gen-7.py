
def jacobsthal_num(n: int):
  if n == 0:
    return 0
  if n == 1:
    return 1
  if n == 2:
    return 1
  a, b = 1, 1
  for _ in range(n-2):
    c = a + b
    a = b
    b = c
  return c


