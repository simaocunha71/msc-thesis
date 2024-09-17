
def validate(num: int) -> bool:
  digits = [int(digit) for digit in str(num)]
  for digit in digits:
    if digit > 1 and digit > digits.count(digit):
      return False
  return True


