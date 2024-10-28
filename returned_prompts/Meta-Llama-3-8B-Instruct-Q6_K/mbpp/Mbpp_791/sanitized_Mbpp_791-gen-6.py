def remove_nested(tup):
  result = []
  for elem in tup:
    if not isinstance(elem, tuple):
      result.append(elem)
  return tuple(result)  # Convert the list back to a tuple