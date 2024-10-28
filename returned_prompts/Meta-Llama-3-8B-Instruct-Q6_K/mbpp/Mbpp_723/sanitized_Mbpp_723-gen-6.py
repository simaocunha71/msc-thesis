def count_same_pair(lst1, lst2):
  return sum([1 for i in range(len(lst1)) if lst1[i] == lst2[i]])