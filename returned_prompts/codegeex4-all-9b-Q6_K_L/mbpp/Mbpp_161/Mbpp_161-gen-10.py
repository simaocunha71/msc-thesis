def remove_elements(test_list, remove_list):
  for i in remove_list:
    while i in test_list:
      test_list.remove(i)
  return test_list

