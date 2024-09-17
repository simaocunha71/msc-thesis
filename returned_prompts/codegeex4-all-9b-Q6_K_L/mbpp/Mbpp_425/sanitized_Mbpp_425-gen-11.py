def count_element_in_list(test_list, test_element):
  count = 0
  for sublist in test_list:
    if test_element in sublist:
      count += 1
  return count