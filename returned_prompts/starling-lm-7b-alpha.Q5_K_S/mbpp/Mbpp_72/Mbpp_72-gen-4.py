
def dif_Square(n):
  if n == 0:
    return False
  for i in range(0, int(n**0.5)+1):
    if i * i - n > 0 and (i * i - n) ** 0.5 == int((i * i - n) ** 0.5):
      return True
  return False


