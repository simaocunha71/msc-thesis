def check_type(tup):
  return all(isinstance(item, type(tup[0])) for item in tup)