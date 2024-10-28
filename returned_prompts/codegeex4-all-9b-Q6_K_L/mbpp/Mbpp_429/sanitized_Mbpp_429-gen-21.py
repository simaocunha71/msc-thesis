def and_tuples(tup1, tup2):
  return tuple(map(lambda x: x[0] and x[1], zip(tup1, tup2)))