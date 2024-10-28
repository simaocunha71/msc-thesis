def multiply_elements(tup: tuple):
  res = tuple([tup[i] * tup[i+1] for i in range(len(tup)-1)])
  return res