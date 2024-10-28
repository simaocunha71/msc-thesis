def max_aggregate(lst):
  scores = {}
  for name, score in lst:
    if name in scores:
      scores[name] += score
    else:
      scores[name] = score
  max_score = max(scores.values())
  return next(name for name, score in lst if score == max_score), max_score