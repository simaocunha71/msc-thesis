def get_equal(test_tup):
  return all(len(tup) == len(test_tup[0]) for tup in test_tup)