
def cummulative_sum(tuples):
  sum = 0
  for t in tuples:
    sum += sum(t)
  return sum


