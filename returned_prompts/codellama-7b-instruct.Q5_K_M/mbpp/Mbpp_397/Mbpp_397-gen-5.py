
def median_numbers(a, b, c):
  median = sorted([a, b, c])
  length = len(median)
  if length % 2 == 0:
    return (median[length // 2 - 1] + median[length // 2]) / 2
  else:
    return median[length // 2]


