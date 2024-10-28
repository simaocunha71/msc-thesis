def remove_nested(tup):
  new_tup = ()
  for i in tup:
    if type(i) == tuple:
      for j in i:
        new_tup += (j,)
    else:
      new_tup += (i,)
  return new_tup