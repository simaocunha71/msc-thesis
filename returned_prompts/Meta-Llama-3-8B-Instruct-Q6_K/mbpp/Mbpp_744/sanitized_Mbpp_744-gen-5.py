def check_none(tup):
  return any(i is None for i in tup)  # or return any(i == None for i in tup) if Python version is 2.7 or earlier