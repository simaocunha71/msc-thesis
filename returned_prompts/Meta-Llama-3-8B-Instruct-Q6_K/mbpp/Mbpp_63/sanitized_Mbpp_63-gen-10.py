def max_difference(tuples):
  return max(abs(b-a) for a,b in tuples) if tuples else None