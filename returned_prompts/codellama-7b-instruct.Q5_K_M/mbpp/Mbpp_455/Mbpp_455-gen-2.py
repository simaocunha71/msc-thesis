
def check_monthnumb_number(monthnumb: int) -> bool:
  if monthnumb in [4, 6, 9, 11]:
    return False
  elif monthnumb == 2:
    return True
  else:
    return True


