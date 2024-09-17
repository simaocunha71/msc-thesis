def find_tuples(test_tup1, test_k):
  return [tup for tup in test_tup1 if all(elem % test_k == 0 for elem in tup)]