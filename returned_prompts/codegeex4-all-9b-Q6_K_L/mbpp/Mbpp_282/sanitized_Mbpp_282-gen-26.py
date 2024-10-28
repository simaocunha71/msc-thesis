def sub_list(test_list1,test_list2):
  if len(test_list1) != len(test_list2):
    return "Lists are not of the same size"
  return [x - y for x, y in zip(test_list1, test_list2)]