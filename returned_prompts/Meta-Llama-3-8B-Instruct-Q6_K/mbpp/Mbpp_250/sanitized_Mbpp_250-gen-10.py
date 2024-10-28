def count_X(tup, x):
  return tup.count(x) if isinstance(tup, tuple) else "Error: Input is not a tuple"  # Check if input is a tuple