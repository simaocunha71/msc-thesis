def add_pairwise(test_tup):
  new_tup = []
  for i in range(len(test_tup)-1):
    new_tup.append(test_tup[i]+test_tup[i+1])
  new_tup.append(test_tup[-1]+test_tup[0])
  return tuple(new_tup)