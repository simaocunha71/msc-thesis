def add_pairwise(tup):
  return tuple(i + j for i, j in zip(tup, tup[1:]))