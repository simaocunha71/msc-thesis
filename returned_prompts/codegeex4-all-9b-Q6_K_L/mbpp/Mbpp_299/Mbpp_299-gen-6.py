def max_aggregate(names_and_scores: list):
  max_score = 0
  max_name = ""
  for name, score in names_and_scores:
    if score > max_score:
      max_score = score
      max_name = name
  return (max_name, max_score)