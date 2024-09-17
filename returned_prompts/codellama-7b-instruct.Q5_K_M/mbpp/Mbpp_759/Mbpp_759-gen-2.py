
def is_decimal(s: str) -> bool:
  try:
    float(s)
    return True
  except:
    return False


