def maximize_elements(test_tuple1, test_tuple2):
  return tuple(max(test_tuple1[i], test_tuple2[i]) for i in range(len(test_tuple1)))