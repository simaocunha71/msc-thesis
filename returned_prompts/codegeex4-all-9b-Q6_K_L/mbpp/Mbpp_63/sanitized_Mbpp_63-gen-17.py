def max_difference(tuples: list) -> int:
  return max(t[1] - t[0] for t in tuples)