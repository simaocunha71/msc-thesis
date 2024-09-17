def count_first_elements(tup: tuple):
  return len([i for i in tup if isinstance(i, int)])