def count_Occurrence(tup: tuple, list1: list) -> int:
  count = 0
  for i in list1:
    count += tup.count(i)
  return count