def validate(n: int) -> bool:
  for digit in str(n):
    if int(digit) < len([d for d in str(n) if d == digit]):
      return False
  return True