def count_first_elements(tup):
  count = 0
  for i in tup:
    if isinstance(i, tuple):
      count += 1
  return count

