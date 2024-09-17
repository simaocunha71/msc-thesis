def find_tuples(tuples: list, k: int) -> list:
  result = [t for t in tuples if all(i % k == 0 for i in t)]
  return result