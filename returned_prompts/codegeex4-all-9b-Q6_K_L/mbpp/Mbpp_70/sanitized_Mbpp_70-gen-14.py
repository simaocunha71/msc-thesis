def get_equal(tuples: tuple) -> bool:
  return all(len(t) == len(tuples[0]) for t in tuples)