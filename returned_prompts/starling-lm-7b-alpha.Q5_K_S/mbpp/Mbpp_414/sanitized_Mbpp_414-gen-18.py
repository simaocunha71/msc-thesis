def overlapping(test_tup1, test_tup2):
  for i in test_tup1:
    if i in test_tup2:
      return True
  return False