def extract_even(tup):
  return tuple(i if isinstance(i, int) and i % 2 == 0 else extract_even(i) if isinstance(i, tuple) else None for i in tup)