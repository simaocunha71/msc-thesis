def dif_Square(n):
  if n < 0:
    return False
  for i in range(int(math.sqrt(n))+1):
    if i*i == n:
      return True
    elif i*i > n:
      break
  for i in range(1, int(math.sqrt(n))+1):
    if (n - i*i) in [j*j for j in range(1, int(math.sqrt(n))+1)]:
      return True
  return False