def dif_Square(num):
  for i in range(1, num):
    j = num - i
    if i ** 2 == j ** 2:
      return True
  return False