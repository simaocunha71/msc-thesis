def union_elements(tup1, tup2):
  union_tup = set(tup1) | set(tup2)
  return tuple(sorted(union_tup))