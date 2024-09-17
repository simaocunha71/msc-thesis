
def count_first_elements(tup):
  count = 0
  for i in tup:
    if isinstance(i, tuple):
      count += count_first_elements(i)
    else:
      count += tup.index(i)
  return count


