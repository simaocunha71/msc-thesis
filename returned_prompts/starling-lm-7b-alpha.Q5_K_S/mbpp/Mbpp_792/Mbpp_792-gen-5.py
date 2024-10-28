
def count_list(test_tup):
  count = 0
  for i in test_tup:
    if isinstance(i, list):
      count += 1
  return count


