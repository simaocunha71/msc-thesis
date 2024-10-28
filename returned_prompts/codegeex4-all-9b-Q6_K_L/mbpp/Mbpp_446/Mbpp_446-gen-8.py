def count_Occurrence(test_tuple,test_list):
  count = 0
  for i in test_list:
    count += test_tuple.count(i)
  return count

