
def extract_even(tup):
  result = []
  for i in tup:
    if isinstance(i, tuple):
      new_tuple = extract_even(i)
      if new_tuple:
        result.append(new_tuple)
    elif i % 2 == 0:
      result.append(i)
  return tuple(result)


