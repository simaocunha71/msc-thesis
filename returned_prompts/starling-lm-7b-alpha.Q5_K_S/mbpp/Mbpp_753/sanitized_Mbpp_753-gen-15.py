def min_k(data:list, k:int) -> list:
  data.sort(key = lambda x: x[1])
  return data[:k]