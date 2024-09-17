def start_withp(lst):
  for pair in lst:
    if pair.startswith('p'):
      return tuple(pair.split())
  return None

