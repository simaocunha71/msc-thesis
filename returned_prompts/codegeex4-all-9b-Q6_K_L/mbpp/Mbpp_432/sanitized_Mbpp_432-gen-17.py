def median_trapezium(a,b,c):
  d = (a+b+c)/2
  median = math.sqrt(d*(d-a)*(d-b)*(d-c))
  return median