def union_elements(test_tup1, test_tup2):
  union_tuple = set(test_tup1) | set(test_tup2)
  return sorted(union_tuple)