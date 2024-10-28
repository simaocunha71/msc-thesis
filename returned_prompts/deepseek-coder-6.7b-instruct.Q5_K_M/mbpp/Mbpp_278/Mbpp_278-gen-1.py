
def count_first_elements(test_tup):
  return sum(isinstance(i, tuple) for i in test_tup)


