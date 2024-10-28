def count_integer(lst):
  count = sum(1 for i in lst if isinstance(i, int))
  return count

