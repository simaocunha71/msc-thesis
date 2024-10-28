def extract_even(tup):
  res = []
  for i in tup:
    if isinstance(i, tuple):
      res.append(extract_even(i))
    elif i % 2 == 0:
      res.append(i)
  return tuple(res)

