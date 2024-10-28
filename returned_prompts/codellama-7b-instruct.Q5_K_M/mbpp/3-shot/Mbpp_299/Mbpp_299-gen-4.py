
def max_aggregate(lst):
  max_name = ''
  max_score = 0
  for name, score in lst:
    if score > max_score:
      max_name = name
      max_score = score
  return (max_name, max_score)


