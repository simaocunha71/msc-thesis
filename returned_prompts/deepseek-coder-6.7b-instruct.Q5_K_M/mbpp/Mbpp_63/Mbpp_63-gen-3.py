
def max_difference(lst):
  return max(max(pair)-min(pair) for pair in lst)


