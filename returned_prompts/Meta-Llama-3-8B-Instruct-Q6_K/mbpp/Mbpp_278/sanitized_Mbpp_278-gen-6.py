def count_first_elements(tup):
  return len([x for x in tup if isinstance(x, tuple) or isinstance(x, list)])