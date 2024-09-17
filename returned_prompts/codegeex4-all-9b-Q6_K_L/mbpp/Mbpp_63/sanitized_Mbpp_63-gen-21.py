def max_difference(tuples: list) -> int:
  max_diff = 0
  for i in range(len(tuples)-1):
    max_diff = max(max_diff, tuples[i+1][0] - tuples[i][1])
  return max_diff