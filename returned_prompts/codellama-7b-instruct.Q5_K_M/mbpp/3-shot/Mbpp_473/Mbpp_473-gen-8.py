
def tuple_intersection(tup_list: list) -> set:
  tup_intersection = set()
  for tup in tup_list:
    tup_intersection.update(tup)
  return tup_intersection


