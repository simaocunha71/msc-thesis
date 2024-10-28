def find_tuples(tuples: list,k: int) -> list:
  return [t for t in tuples if all(n % k == 0 for n in t)]