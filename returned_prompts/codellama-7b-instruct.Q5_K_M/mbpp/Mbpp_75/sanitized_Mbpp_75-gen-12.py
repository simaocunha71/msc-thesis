def find_tuples(tuples: list, k: int) -> list:
  return list(filter(lambda x: all(i%k==0 for i in x), tuples))