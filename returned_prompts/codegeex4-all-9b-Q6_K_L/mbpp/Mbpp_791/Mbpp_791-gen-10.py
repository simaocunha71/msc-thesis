def remove_nested(tup: tuple):
  new_tup = ()
  for item in tup:
    if not isinstance(item, tuple):
      new_tup += (item,)
  return new_tup

