def find_tuples(test_tup, k):
  return [tup for tup in test_tup if all(el % k == 0 for el in tup)]