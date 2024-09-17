
def add_pairwise(test_tup):
  return tuple(map(sum, zip(test_tup, test_tup[1:])))


