def is_Sum_Of_Powers_Of_Two(n):
  if n==0:
    return False
  for i in range(1,n):
    if n == 2**i:
      return True
    if n < 2**i:
      return False
  return False