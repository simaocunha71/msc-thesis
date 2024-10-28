def and_tuples(tup1, tup2):
  result = []
  for a, b in zip(tup1, tup2):
    if a and b:
      result.append(tup1.index(a))
    else:
      result.append(0)
  return tuple(result) if result else (0,)  # added this line to handle edge case where result is empty