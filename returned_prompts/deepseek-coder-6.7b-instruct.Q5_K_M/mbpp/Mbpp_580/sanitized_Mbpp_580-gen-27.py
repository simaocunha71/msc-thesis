def extract_even(tup):
  new_tup = []
  for i in tup:
    if isinstance(i, tuple):
      new_tup.append(extract_even(i))
    elif i % 2 == 0:
      new_tup.append(i)
  return tuple(new_tup)