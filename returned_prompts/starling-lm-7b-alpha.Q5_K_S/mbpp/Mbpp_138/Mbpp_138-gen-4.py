
def is_Sum_Of_Powers_Of_Two(n):
  while n:
    if n % 2 != 0:
      return False
    n //= 2
  return True


