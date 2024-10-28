
def is_Sum_Of_Powers_Of_Two(num):
  if num == 0:
    return False
  if num == 1:
    return True
  if num % 2 == 0:
    return is_Sum_Of_Powers_Of_Two(num // 2)
  return is_Sum_Of_Powers_Of_Two(num // 2) and num % 2 != 0


