
def union_elements(test_tup1, test_tup2):
  output = list(set(test_tup1) | set(test_tup2))
  return tuple(sorted(output))


