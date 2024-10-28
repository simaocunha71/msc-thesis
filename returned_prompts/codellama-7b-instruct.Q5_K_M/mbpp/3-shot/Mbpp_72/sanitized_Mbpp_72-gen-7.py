def dif_Square(n):
  for i in range(1, n + 1):
    j = sqrt(n - i)
    if int(j) == j:
      return True
  return False