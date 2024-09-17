def max_difference(tuple_list):
  max_diff = 0
  for tup in tuple_list:
    diff = tup[0] - tup[1]
    if diff > max_diff:
      max_diff = diff
  return max_diff