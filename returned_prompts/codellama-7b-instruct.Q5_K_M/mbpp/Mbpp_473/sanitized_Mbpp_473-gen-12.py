def tuple_intersection(tuple_list: list) -> set:
  return set.intersection(*map(set, tuple_list))