def find_tuples(test_list, k):
  return [t for t in test_list if all(i % k == 0 for i in t)]