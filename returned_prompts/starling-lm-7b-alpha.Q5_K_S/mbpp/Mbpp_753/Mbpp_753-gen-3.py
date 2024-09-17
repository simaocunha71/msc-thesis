
def min_k(records: list, k: int) -> list:
  records.sort(key=lambda x: x[1])
  return records[:k]


