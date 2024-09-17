def min_k(tuples: list, n: int) -> list:
  return sorted(tuples, key=lambda x: x[1])[:n]


