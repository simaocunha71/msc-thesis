def start_withp(lst):
  for word in lst:
    if word.startswith('p'):
      return word.split()
  return None