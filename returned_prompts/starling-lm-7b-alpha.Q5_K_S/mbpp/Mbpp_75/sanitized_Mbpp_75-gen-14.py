def find_tuples(test_tups, k):
  return [tup for tup in test_tups if all(x%k == 0 for x in tup)]