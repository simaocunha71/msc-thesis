def tuple_intersection(tup1: list,tup2: list) -> set:
  return set(map(tuple, set(map(list, tup1)) & set(map(list, tup2))))