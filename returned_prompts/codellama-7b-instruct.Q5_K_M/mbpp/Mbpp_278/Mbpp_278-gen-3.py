
def count_first_elements(tup):
  count = 0
  for i in tup:
    if isinstance(i, tuple):
      break
    else:
      count += 1
  return count

