def substract_elements(test_tup1, test_tup2):
  return tuple(test_tup1[i] - test_tup2[i] for i in range(len(test_tup1)))