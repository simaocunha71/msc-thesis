def min_k(tup: list, k: int) -> list:
  return sorted(tup, key=lambda x: x[1])[:k]