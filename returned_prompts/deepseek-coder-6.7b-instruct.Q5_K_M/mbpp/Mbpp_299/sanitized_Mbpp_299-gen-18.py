def max_aggregate(tuples):
  d = {}
  for name, score in tuples:
    if name in d:
      d[name] += score
    else:
      d[name] = score
  max_score = max(d.values())
  for key in d:
    if d[key] == max_score:
      return (key, max_score)