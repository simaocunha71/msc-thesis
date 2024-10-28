
def prime_num(n: int) -> bool:
  if n == 1:
    return False
  if n == 2:
    return True
  if n % 2 == 0:
    return False
  sqrt = int(n ** 0.5)
  for i in range(3, sqrt + 1, 2):
    if n % i == 0:
      return False
  return True


