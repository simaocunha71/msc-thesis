def union_elements(tup1, tup2):
  return tuple(sorted(set(tup1 + tup2)))  # Convert to set to remove duplicates and then sorted to sort the elements.  # Convert to tuple to return a tuple.