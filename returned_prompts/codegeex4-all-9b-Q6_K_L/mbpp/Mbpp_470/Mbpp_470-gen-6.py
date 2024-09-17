def add_pairwise(test_tuple):
  test_list = list(test_tuple)
  for i in range(len(test_list)-1):
    test_list[i] += test_list[i+1]
  return tuple(test_list)


