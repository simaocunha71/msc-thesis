def count_Occurrence(tup, lst):
  return sum(tup.count(i) for i in lst) if all(i in tup for i in lst) else 'All elements not found in tuple'