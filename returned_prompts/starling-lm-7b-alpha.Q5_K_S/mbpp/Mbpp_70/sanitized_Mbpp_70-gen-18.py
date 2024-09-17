def get_equal(test_tup):
  if len(set([len(tup) for tup in test_tup])) == 1:
    return True
  else:
    return False