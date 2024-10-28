def remove_nested(test_tup):
  return tuple([i for i in test_tup if not isinstance(i, tuple)])