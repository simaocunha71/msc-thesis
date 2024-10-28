
def is_decimal(num_str: str) -> bool:
  if len(num_str) > 3:
    return False
  if '.' in num_str:
    if len(num_str) - num_str.index('.') > 2:
      return False
  return True


