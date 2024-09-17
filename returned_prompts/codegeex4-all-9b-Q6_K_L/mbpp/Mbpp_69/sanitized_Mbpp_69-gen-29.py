def is_sublist(test_list1, test_list2):
  if len(test_list2) > len(test_list1):
    return False
  for i in range(len(test_list1)):
    if test_list1[i:i+len(test_list2)] == test_list2:
      return True
  return False