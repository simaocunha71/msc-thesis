def check_occurences(tuples: list) -> dict:
  return dict((x, tuples.count(x)) for x in set(tuples))