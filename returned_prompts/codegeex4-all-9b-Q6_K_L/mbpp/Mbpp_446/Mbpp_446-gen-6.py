def count_Occurrence(test_tup, test_list):
  count = 0
  for i in test_list:
    count += test_tup.count(i)
  return count