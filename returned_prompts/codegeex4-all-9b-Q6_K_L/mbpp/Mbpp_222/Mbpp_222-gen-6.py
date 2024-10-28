def check_type(test_tuple):
  if len(set(type(x) for x in test_tuple)) == 1:
    return True
  else:
    return False