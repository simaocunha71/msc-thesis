def is_Sum_Of_Powers_Of_Two(n):
  if n == 0:
    return True
  if n & (n-1) == 0:
    return True
  return False