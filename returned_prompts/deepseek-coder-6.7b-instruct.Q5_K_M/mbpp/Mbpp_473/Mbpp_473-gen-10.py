
def tuple_intersection(tuples1: list, tuples2: list) -> set:
  intersection = set()
  for t1 in tuples1:
    for t2 in tuples2:
      if set(t1) == set(t2):
        intersection.add(t1)
  return intersection


