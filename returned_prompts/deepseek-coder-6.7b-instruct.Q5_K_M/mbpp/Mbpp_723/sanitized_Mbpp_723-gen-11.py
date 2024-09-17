def count_same_pair(lst1, lst2):
  return sum(1 for a, b in zip(lst1, lst2) if a == b)