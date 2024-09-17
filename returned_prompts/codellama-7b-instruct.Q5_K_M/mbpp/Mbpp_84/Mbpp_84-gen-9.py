
def sequence(n):
  if n == 1:
    return 1
  elif n == 2:
    return 1
  else:
    return sequence(newman_conway(n-1)) + sequence(newman_conway(n-2))


