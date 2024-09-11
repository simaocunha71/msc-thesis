def count_first_elements(tup):
  count = 0
  for element in tup:
    if isinstance(element, tuple):
      break
    count += 1
  return count