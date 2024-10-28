def remove_kth_element(lst, k):
  return lst[:k-1] + lst[k:]  # remove the kth element and return the list