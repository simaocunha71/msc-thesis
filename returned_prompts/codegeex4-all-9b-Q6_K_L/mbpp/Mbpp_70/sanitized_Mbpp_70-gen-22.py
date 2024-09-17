def get_equal(tuples: list) -> bool:
  return all(len(t) == len(tuples[0]) for t in tuples)