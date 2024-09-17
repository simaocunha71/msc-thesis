def extract_even(nested_tuple: tuple) -> tuple:
  return tuple(filter(lambda x: not isinstance(x, tuple) or x[1] % 2 == 0, nested_tuple))