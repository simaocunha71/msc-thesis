def check_distinct(test_tuple):
  if len(set(test_tuple)) == len(test_tuple):
    return True
  else:
    return False