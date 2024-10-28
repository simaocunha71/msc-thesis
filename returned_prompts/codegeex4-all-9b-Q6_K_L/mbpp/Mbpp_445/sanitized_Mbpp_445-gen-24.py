def index_multiplication(tup1, tup2):
  if len(tup1) != len(tup2):
    raise ValueError("Both tuples must have the same length")
  return tuple((a*b for a, b in zip(tup1, tup2)))