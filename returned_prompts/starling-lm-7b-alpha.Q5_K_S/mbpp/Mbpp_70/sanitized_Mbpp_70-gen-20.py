def get_equal(test_tup_list):
  if all(map(lambda x: len(x) == len(test_tup_list[0]), test_tup_list)):
    return True
  else:
    return False