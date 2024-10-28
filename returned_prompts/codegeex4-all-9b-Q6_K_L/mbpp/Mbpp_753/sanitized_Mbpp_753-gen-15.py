def min_k(tuples: list,k: int) -> list:
  return sorted(tuples, key=lambda x: x[1])[:k]