
def get_equal(test_tup):
  if len(set(map(len, test_tup))) == 1:
    return True
  else:
    return False


