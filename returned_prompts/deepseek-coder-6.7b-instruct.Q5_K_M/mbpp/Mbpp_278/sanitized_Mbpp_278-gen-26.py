def count_first_elements(test_tup):
  count = 0
  for i in test_tup:
    if isinstance(i, tuple):
      break
    count += 1
  return count