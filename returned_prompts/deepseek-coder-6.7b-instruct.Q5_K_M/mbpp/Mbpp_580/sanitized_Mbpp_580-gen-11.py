def extract_even(nested_tuple):
  result = []
  for i in nested_tuple:
    if isinstance(i, tuple):
      new_tuple = extract_even(i)
      if new_tuple:
        result.append(new_tuple)
    elif i % 2 == 0:
      result.append(i)
  return tuple(result)