def add_pairwise(test_tup):
  return tuple(map(lambda x, y: x + y, test_tup[0:len(test_tup)-1], test_tup[1:]))