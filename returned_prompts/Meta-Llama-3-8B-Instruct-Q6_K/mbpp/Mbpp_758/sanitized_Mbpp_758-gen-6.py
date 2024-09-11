from collections import Counter
def unique_sublists(lst):
  return dict(Counter(map(tuple, lst)))  # convert lists to tuples and count their occurrences