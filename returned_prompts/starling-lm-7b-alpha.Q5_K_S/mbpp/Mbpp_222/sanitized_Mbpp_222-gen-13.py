def check_type(tup):
  return all(map(lambda x: type(x) == type(tup[0]), tup))