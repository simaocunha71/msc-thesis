
def is_woodall(n: int) -> bool:
  if n < 100:
    return False
  if n % 100 == 0:
    return False
  if n % 10 == 0:
    return False
  return True


