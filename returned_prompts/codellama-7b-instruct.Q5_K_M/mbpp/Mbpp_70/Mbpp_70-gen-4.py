
def get_equal(tuples: list) -> bool:
  return len(set(len(tup) for tup in tuples)) == 1


