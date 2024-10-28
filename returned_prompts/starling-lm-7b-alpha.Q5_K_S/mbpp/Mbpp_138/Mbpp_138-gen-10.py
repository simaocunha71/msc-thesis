
def is_Sum_Of_Powers_Of_Two(num: int) -> bool:
  while num != 0:
    if num % 2 != 0:
      return False
    num = num // 2
  return True


