
def max_aggregate(test_list):
  aggregate = 0
  for name, score in test_list:
    if score > aggregate:
      aggregate = score
  return (name, aggregate)


