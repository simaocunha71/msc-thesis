def dif_Square(n):
  for i in range(1, int(n ** 0.5) + 1):
    j = int((n - i ** 2) ** 0.5)
    if i ** 2 + j ** 2 == n:
      return True
  return False