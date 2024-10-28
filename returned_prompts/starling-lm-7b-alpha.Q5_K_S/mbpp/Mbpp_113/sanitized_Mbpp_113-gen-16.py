def check_integer(str_: str) -> bool:
  try:
    int(str_)
    return True
  except ValueError:
    return False