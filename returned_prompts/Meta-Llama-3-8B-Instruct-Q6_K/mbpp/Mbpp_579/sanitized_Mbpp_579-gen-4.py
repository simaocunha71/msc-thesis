def find_dissimilar(test_tup1, test_tup2):
  set1 = set(test_tup1)
  set2 = set(test_tup2)
  return tuple(sorted(list(set1.symmetric_difference(set2))))