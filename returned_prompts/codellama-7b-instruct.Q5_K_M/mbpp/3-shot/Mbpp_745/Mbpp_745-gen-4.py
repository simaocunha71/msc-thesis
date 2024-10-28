
def divisible_by_digits(startnum: int, endnum: int) -> list:
  result = []
  for i in range(startnum, endnum+1):
    if is_divisible(i):
      result.append(i)
  return result

def is_divisible(num: int) -> bool:
  if num == 0:
    return False
  for i in str(num):
    if num % int(i) != 0:
      return False
  return True


