def max_difference(tuples):
  return max(abs(a - b) for a, b in tuples) if tuples else None