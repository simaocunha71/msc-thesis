def check_smaller(test_tup1, test_tup2):
  if len(test_tup1) != len(test_tup2):
    return False
  for i in range(len(test_tup1)):
    if test_tup1[i] <= test_tup2[i]:
      return False
  return True