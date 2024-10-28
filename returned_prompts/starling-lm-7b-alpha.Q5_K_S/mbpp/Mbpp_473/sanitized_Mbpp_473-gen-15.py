def tuple_intersection(tups: list, tups2: list):
  intersection_tups = set(tups) & set(tups2)
  return list(intersection_tups)