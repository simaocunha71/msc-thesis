def check_integer(string: str) -> bool:
  try:
    int(string)
    return True
  except ValueError:
    return False