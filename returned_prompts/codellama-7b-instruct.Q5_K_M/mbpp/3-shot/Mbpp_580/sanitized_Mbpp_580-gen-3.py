def extract_even(nested_tuple):
  new_tuple = []
  for i in nested_tuple:
    if type(i) == tuple:
      new_tuple.append(extract_even(i))
    elif i % 2 == 0:
      new_tuple.append(i)
  return tuple(new_tuple)