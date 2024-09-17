
def tuple_intersection(tuples1, tuples2):
  sets = [set(t) for t in tuples1+tuples2]
  return set.intersection(*sets)


