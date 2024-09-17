def min_k(tup_list: list, k: int) -> list:
  return sorted(tup_list, key=lambda x: x[1])[:k]