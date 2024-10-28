def count_Occurrence(tuple, elements):
  count = 0
  for element in elements:
    count += tuple.count(element)
  return count