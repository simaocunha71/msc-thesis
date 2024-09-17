
def max_aggregate(tup_list):
  max_name, max_score = None, 0
  for name, score in tup_list:
    if score > max_score:
      max_score = score
      max_name = name
  return (max_name, max_score)


