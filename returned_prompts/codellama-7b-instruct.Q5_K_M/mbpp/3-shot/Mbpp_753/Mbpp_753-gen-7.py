
def min_k(my_list: list, k: int) -> list:
  return sorted(my_list, key=lambda x: x[1])[:k]


