
def max_difference(tuples):
  diff = []
  for t in tuples:
    diff.append(t[1] - t[0])
  return max(diff)


