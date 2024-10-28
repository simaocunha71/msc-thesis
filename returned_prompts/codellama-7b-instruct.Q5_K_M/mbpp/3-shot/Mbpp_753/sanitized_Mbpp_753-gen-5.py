def min_k(test_tup_list: list, k: int) -> list:
  return sorted(test_tup_list, key=lambda x: x[1])[:k]