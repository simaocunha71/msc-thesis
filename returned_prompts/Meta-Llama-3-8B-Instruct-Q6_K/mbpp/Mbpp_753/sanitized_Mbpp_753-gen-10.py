def min_k(tuples, k):
  return sorted(tuples, key=lambda x: x[1])[:k]  # sort by second element and return first k elements