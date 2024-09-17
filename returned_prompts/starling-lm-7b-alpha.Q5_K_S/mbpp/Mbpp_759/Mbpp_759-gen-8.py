
def is_decimal(num: str) -> bool:
  if len(num.split(".")) != 2:
    return False
  if len(num.split(".")[1]) != 2:
    return False
  for i in num.split(".")[1]:
    if not i.isdigit():
      return False
  return True


