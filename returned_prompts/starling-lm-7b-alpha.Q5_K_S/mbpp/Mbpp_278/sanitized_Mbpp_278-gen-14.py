def count_first_elements(test_tup):
  count = 0
  for i in test_tup:
    if isinstance(i, tuple):
      count += len(test_tup[:test_tup.index(i)])
  return count