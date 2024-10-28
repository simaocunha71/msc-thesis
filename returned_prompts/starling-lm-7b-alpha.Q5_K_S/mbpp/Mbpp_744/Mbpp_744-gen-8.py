
def check_none(tup: tuple) -> bool:
  for elem in tup:
    if elem is None:
      return True
  return False


