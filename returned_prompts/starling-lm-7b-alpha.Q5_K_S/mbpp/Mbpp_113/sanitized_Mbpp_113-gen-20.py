def check_integer(num:str) -> bool:
  try:
    int(num)
    return True
  except ValueError:
    return False