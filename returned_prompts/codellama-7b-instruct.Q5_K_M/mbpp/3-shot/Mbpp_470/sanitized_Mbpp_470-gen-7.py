def add_pairwise(tup):
  new_tup = ()
  for i in range(len(tup)-1):
    new_tup += (tup[i] + tup[i+1],)
  return new_tup