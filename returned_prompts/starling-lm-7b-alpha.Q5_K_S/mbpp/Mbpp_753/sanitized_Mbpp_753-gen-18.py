def min_k(test_tup, k):
  test_tup.sort(key=lambda x: x[1])
  return test_tup[:k]