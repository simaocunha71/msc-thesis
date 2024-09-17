def tuple_intersection(tup_list):
  intersection = set()
  for tup in tup_list:
    intersection = intersection.union(tup)
  return intersection