
def is_woodall(n: int) -> bool:
  while n > 0:
    if n % 10 != (n % 5):
      return False
    n = n // 10
  return True


