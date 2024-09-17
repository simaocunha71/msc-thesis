def add_pairwise(tup):
  return tuple(sum(x) for x in zip(tup, tup[1:]))