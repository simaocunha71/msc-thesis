def get_equal(test_tup_list):
  return all(map(lambda x: len(x) == test_tup_list[0], test_tup_list))