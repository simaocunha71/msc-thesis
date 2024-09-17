
def and_tuples(test_tup1, test_tup2):
  return tuple(i for i, (a, b) in enumerate(zip(test_tup1, test_tup2)) if a and b)


