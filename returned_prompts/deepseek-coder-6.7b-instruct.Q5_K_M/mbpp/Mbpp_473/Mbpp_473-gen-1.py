
def tuple_intersection(tuples1, tuples2):
  return set(tuple(sorted(t)) for t in set(tuples1).intersection(set(tuples2)))


