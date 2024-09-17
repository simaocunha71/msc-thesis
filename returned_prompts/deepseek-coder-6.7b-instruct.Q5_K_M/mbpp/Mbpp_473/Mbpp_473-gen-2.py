
def tuple_intersection(tuples1, tuples2):
  return set(tuple(sorted(t)) for t in (set(t) for t in tuples1) & (set(t) for t in tuples2))


