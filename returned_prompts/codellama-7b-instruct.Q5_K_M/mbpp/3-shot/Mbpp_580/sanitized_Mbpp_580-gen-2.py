def extract_even(tup):
  return tuple(filter(lambda x: not isinstance(x, tuple) or not x % 2, tup))