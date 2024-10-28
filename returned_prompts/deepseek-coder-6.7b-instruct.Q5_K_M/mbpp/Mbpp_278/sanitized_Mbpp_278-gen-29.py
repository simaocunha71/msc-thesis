def count_first_elements(tup):
  return sum(isinstance(i, tuple) for i in tup)