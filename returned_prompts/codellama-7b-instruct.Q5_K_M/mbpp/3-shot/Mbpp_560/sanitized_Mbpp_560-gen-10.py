def union_elements(test_tup1, test_tup2):
  union_list = list(set(test_tup1) | set(test_tup2))
  union_list.sort()
  return tuple(union_list)