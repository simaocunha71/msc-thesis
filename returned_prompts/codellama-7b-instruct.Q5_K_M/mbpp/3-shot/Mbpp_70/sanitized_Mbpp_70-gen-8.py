def get_equal(tuples: list) -> bool:
  return all(len(tuples[0]) == len(t) for t in tuples)