def min_val(lst):
  return min(lst, key=lambda x: (isinstance(x, int), x))