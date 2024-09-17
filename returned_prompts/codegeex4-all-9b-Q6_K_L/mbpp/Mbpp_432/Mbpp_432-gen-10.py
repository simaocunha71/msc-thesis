def median_trapezium(a,b,c,d):
  # Find the mid-point of the longer base
  if b > a:
    longer_base = (a + b) / 2
  else:
    longer_base = (b + a) / 2

  # Find the mid-point of the shorter base
  if d > c:
    shorter_base = (c + d) / 2
  else:
    shorter_base = (d + c) / 2

  # Calculate the median length of the trapezium
  median = (longer_base + shorter_base) / 2

  return median

