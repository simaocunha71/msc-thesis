
def get_equal(test_tup):
  return all(map(lambda x: len(x) == len(test_tup[0]), test_tup))


