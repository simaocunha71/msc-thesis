def extract_even(nested_tuple):
  if isinstance(nested_tuple, tuple):
    return tuple(extract_even(x) if isinstance(x, tuple) else x % 2 == 0 for x in nested_tuple)
  else:
    return nested_tuple % 2 == 0

