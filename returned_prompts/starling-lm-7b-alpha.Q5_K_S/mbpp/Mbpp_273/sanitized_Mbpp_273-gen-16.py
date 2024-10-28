def substract_elements(test_tup1, test_tup2):
  result_tup = []
  for i in range(len(test_tup1)):
    result_tup.append(test_tup1[i] - test_tup2[i])
  return tuple(result_tup)