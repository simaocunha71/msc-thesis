
def sequence(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return sequence(n-1) + sequence(n-2)


