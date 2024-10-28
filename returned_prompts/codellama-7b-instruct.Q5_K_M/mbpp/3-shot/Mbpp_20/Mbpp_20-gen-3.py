
def is_woodall(n):
  str_num = str(n)
  for digit in str_num:
    if int(digit) != 3:
      return False
  return True


