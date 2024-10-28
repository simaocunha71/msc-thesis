
def validate(n):
  num_str = str(n)
  for i, digit in enumerate(num_str):
    if i+1 > int(digit):
      return False
  return True


