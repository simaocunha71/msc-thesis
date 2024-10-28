def cummulative_sum(tuples):
  return sum(sum(i) for i in tuples)  # or sum(sum(t) for t in tuples)