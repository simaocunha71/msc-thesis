def median_numbers(a, b, c):
  if a >= b and a >= c:
    if b >= c:
      return b
    else:
      return c
  elif b >= a and b >= c:
    if a >= c:
      return a
    else:
      return c
  else:
    if a >= b:
      return a
    else:
      return b
  return (a+b+c)/3.0