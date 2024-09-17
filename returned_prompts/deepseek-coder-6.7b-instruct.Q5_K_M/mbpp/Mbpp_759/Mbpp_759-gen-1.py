
def is_decimal(s: str) -> bool:
  try:
    float_s = float(s)
    return True
  except ValueError:
    return False


