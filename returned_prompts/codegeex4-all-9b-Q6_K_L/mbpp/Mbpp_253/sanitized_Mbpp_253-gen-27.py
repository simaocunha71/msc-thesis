def count_integer(lst):
  count = 0
  for i in lst:
    if isinstance(i, int):
      count += 1
  return count