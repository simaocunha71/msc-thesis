def check_none(test_tuple):
  if any(x is None for x in test_tuple):
    return True
  else:
    return False