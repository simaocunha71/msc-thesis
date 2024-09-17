def count_Occurrence(tup: tuple, lst: list) -> int:
  count = 0
  for i in tup:
    if i in lst:
      count += 1
  return count

