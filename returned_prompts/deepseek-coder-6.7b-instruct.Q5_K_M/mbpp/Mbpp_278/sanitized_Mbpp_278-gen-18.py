def count_first_elements(tup):
  return sum(1 for i in tup if not isinstance(i, tuple))