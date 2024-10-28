def count_Occurrence(test_tup, test_list):
  count = 0
  for i in test_list:
    for j in test_tup:
      if i == j:
        count += 1
  return count

