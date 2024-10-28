def min_k(tuple_list, k):
  sorted_tuple_list = sorted(tuple_list, key=lambda x: x[1])
  return sorted_tuple_list[:k]  # returns the first k elements of the sorted list