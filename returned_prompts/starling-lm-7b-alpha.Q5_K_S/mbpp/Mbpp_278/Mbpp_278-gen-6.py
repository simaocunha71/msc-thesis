
def count_first_elements(tup: tuple) -> int:
  count = 0
  for i in tup:
    if isinstance(i, tuple):
      count += count_first_elements(i)
    else:
      count += 1
  return count


