
def extract_even(tup):
  res = []
  for i in tup:
    if isinstance(i, tuple):
      res.append(tuple(filter(lambda x: x % 2 == 0, i)))
    elif i % 2 == 0:
      res.append(i)
  return tuple(res)


