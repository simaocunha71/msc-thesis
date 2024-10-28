
def is_Sum_Of_Powers_Of_Two(n: int) -> bool:
  while n:
    if n == 1:
      return True
    if n % 2 != 0:
      return False
    n = n >> 1
  return False


