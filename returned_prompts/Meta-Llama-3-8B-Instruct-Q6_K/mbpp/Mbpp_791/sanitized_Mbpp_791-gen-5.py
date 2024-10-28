def remove_nested(tup):
  new_tup = tup
  for i in range(len(tup)):
    if isinstance(tup[i], tuple):
      new_tup = new_tup[:i] + new_tup[i+1:]
  return new_tup