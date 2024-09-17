
def add_pairwise(tup):
  return tuple(sum(x) for x in zip(tup[::2], tup[1::2]))


