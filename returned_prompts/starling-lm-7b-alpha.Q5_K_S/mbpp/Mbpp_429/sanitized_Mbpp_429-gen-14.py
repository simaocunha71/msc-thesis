def and_tuples(tup1, tup2):
  return tuple(map(min, zip(tup1, tup2)))