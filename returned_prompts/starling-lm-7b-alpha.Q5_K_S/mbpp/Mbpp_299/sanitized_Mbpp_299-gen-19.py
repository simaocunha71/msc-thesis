def max_aggregate(tuples):
  name, score = max(tuples, key=lambda tup: tup[1])
  return (name, sum(tup[1] for tup in tuples))