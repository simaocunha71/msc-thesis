def dif_Square(num):
  for i in range(1, num):
    j = int(num - i)
    if i**2 + j**2 == num:
      return True
  return False