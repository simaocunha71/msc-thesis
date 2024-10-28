def tuple_intersection(test_tup1, test_tup2):
  intersection_set = set(test_tup1) & set(test_tup2)
  intersection_tuple = tuple(intersection_set)
  return intersection_tuple