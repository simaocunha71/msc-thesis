def min_k(records: list,k: int) -> list:
  return sorted(records,key=lambda x:x[1])[:k]