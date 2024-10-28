def check_none(tup: tuple) -> bool:
  for i in tup:
    if i is None:
      return True
  return False