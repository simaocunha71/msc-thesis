def min_k(tuples: list,k: int) -> list:
  min_k_tuples = sorted(tuples, key=lambda x: x[1])[:k]
  return min_k_tuples

