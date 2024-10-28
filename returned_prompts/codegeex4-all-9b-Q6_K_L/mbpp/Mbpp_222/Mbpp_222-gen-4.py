def check_type(tup: tuple) -> bool:
  return all(type(tup[i]) == type(tup[0]) for i in range(len(tup)))

