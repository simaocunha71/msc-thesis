def add_pairwise(tup):
  return tuple(map(lambda x, y: x + y, tup[::1], tup[1::1]))