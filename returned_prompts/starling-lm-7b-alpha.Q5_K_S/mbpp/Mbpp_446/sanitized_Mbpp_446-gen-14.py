def count_Occurrence(tup: tuple, lst: list) -> int:
  counter = 0
  for elem in lst:
    for i in tup:
      if elem == i:
        counter += 1
  return counter