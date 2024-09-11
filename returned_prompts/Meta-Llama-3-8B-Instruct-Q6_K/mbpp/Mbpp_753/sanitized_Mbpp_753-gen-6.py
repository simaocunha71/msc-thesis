def min_k(record_list, k):
  record_list.sort(key=lambda x: x[1])
  return record_list[:k]  # return the first k elements