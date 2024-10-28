def and_tuples(tup1, tup2):
  return tuple(x for x in zip(tup1, tup2) if x[0] == x[1])