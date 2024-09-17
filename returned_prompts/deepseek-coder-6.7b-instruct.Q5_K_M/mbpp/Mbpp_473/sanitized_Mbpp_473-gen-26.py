def tuple_intersection(tuples1: list, tuples2: list) -> set:
  return set(tuple(sorted(t)) for t in set(tuples1) & set(tuples2))