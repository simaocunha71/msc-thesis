def find_tuples(tuples: list, k: int) -> list:
  divisible_tuples = [t for t in tuples if all(i % k == 0 for i in t)]
  return divisible_tuples