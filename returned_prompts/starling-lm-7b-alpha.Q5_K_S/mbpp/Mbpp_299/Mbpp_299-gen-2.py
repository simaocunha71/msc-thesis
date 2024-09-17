
def max_aggregate(scores: list) -> tuple:
  max_score = max(scores, key = lambda x: x[1])
  return max_score


