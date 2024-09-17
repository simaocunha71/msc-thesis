
def tuple_to_dict(test_tup):
  test_dict = {}
  for i in range(0, len(test_tup), 2):
    test_dict[test_tup[i]] = test_tup[i + 1]
  return test_dict


