def extract_even(tup):
  res = []
  for i in tup:
    if isinstance(i, tuple):
      new_tuple = extract_even(i)
      if new_tuple:
        res.append(new_tuple)
    elif i % 2 == 0:
      res.append(i)
  return tuple(res)