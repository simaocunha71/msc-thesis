def find_dissimilar(test_tup1, test_tup2):
  return tuple(set(test_tup1)^set(test_tup2))