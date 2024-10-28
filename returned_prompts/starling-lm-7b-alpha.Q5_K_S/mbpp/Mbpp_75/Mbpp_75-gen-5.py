
def find_tuples(test_tup1, k):
  return [tup for tup in test_tup1 if all(i % k == 0 for i in tup)]


