def maximize_elements(test_tup1, test_tup2):
  return tuple(sorted(zip(test_tup1, test_tup2), key=lambda x: x[0] + x[1], reverse=True))