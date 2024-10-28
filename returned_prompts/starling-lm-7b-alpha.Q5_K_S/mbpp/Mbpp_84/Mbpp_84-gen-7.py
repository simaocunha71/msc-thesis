
def sequence(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  if n == 2:
    return 1
  return sequence(n-1) + sequence(n-2) + sequence(n-3)


