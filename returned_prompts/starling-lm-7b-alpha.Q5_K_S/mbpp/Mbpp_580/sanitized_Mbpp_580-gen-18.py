def extract_even(mixed_tuple):
  return tuple(filter(lambda x: isinstance(x, (int, tuple)) and all(i % 2 == 0 for i in x), mixed_tuple))