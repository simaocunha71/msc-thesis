def get_equal(tuples):
  return all(len(tup) == len(tuples[0]) for tup in tuples)