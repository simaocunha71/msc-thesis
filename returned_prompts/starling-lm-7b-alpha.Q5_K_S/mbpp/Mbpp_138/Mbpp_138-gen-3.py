
def is_Sum_Of_Powers_Of_Two(n: int) -> bool:
  while(n):
    if(n%2 == 1):
      return True
    n = n//2
  return False


