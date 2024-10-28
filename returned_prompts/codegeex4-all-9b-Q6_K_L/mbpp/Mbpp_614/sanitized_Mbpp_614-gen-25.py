def cummulative_sum(tuples: tuple) -> int:
  return sum(sum(t) for t in tuples)