def min_k(test_list: list, k: int) -> list:
  return sorted(test_list, key=lambda x: x[1])[:k]