
def min_k(tup_list: list, k: int) -> list:
  sorted_list = sorted(tup_list)
  return [i[1] for i in sorted_list[:k]]


