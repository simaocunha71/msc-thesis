def validate(n):
  for digit in str(n):
    if str(n).count(digit) > int(digit):
      return False
  return True