
def sequence(n):
  if n <= 2:
    return 1
  return sequence(sequence(n-1)) + sequence(n-sequence(n-1))


