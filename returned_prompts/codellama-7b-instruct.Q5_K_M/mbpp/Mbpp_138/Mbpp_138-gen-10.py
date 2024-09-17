
def is_Sum_Of_Powers_Of_Two(n):
  if n==0:
    return False
  while n>0:
    if n&1==1:
      return False
    n>>=1
  return True


