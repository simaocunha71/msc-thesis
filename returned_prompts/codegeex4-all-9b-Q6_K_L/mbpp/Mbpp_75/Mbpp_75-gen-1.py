def find_tuples(tuples: list, k: int) -> list:
  return [tup for tup in tuples if all(i % k == 0 for i in tup)]

