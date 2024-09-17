def dif_Square(n: int) -> bool:
  for i in range(1, int(math.sqrt(n))+1):
    if (n + i) % 2 == 0:
      return True
  return False

