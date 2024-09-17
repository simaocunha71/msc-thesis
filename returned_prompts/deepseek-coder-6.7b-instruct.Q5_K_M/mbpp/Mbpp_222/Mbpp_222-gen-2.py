
def check_type(tup):
  return all(isinstance(x, type(tup[0])) for x in tup)


