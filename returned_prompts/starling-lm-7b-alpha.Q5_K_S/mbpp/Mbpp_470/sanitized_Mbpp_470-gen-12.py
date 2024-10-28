def add_pairwise(test_tup):
  return tuple(sum(pair) for pair in zip(test_tup, test_tup[1:])) + (test_tup[0]+test_tup[1])