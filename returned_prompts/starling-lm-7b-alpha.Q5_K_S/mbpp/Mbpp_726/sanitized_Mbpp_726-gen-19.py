def multiply_elements(tup):
  l = len(tup)
  return tuple((tup[i]*tup[i+1]) for i in range(l-1))