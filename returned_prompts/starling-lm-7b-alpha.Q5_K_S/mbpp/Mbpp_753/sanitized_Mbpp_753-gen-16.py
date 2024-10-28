def min_k(tuple_list,k):
  sorted_list = sorted(tuple_list, key=lambda x: x[1])
  return sorted_list[:k]