def validate(n: int) -> bool:
  num_digits = len(str(n))
  for i in range(num_digits):
    if str(n).count(str(n)[i]) > str(n)[i]:
      return False
  return True