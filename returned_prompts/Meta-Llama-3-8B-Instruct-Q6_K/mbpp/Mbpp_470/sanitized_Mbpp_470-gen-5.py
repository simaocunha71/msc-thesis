def add_pairwise(tup):
  return tuple(sum(i) for i in zip(tup, tup[1:]))