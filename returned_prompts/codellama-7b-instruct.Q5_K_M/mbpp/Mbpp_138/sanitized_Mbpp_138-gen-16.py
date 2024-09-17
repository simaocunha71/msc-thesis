def is_Sum_Of_Powers_Of_Two(num: int) -> bool:
  while(num>0):
    if num & 1 == 1:
      return False
    num >>= 1
  return True