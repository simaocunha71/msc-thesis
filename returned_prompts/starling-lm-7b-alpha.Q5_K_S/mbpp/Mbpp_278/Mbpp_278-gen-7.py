
def count_first_elements(tup: tuple) -> int:
  count = 0
  for i in tup:
    if type(i) == tuple:
      count += len(i)
    else:
      count += 1
  return count


