def add_pairwise(tup):
  return tuple(x+y for x, y in zip(tup, tup[1:]))

