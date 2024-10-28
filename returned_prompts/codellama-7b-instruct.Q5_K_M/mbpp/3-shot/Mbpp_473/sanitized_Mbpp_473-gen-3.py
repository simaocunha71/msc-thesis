def tuple_intersection(tuple_list: list) -> set:
  intersection = set()
  for tuple in tuple_list:
    intersection.update(tuple)
  return intersection