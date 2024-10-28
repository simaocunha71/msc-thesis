def count_Occurrence(tup: tuple, lst: list) -> int:
  count = 0
  for i in lst:
    count += tup.count(i)
  return count