def multiply_elements(tup):
  res = []
  for i in range(len(tup)-1):
    res.append(tup[i]*tup[i+1])
  return tuple(res)