def check_type(tup):
  return all(type(tup[0]) == type(x) for x in tup)

