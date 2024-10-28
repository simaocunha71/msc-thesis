
def opposite_Signs(num1: int, num2: int) -> bool:
  if num1 > 0 and num2 < 0:
    return True
  if num1 < 0 and num2 > 0:
    return True
  else:
    return False


