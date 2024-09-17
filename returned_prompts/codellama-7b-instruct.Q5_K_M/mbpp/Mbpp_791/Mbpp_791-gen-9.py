
def remove_nested(tup):
  result = []
  for i in tup:
    if isinstance(i, tuple):
      result.extend(remove_nested(i))
    else:
      result.append(i)
  return tuple(result)


