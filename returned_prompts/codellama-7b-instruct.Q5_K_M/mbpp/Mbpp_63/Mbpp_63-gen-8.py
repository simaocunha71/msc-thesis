
def max_difference(pairs):
  max_diff = 0
  for pair in pairs:
    diff = pair[1] - pair[0]
    if diff > max_diff:
      max_diff = diff
  return max_diff


