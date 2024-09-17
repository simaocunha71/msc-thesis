def sequence(n):
  if n == 1:
    return 1
  elif n == 2:
    return 1
  else:
    return sequence(sequence(n-2)) + sequence(n-sequence(n-2))