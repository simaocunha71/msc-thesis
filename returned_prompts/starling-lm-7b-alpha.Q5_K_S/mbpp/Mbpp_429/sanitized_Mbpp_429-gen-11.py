def and_tuples(tup1, tup2):
  return tuple(min(i, j) for i, j in zip(tup1, tup2))