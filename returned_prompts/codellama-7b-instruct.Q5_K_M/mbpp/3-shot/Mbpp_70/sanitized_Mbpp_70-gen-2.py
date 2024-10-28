def get_equal(my_tuples: list) -> bool:
  if len(set(map(len, my_tuples))) == 1:
    return True
  else:
    return False