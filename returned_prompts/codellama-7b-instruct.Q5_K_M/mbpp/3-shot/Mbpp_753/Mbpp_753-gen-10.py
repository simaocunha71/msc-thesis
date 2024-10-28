
def min_k(tuple_list: list, k: int) -> list:
  return sorted(tuple_list, key=lambda x: x[1])[:k]


