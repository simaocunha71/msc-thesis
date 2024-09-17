def last(a, b):
  try:
    return len(a) - 1 - a[::-1].index(b)
  except ValueError:
    return -1