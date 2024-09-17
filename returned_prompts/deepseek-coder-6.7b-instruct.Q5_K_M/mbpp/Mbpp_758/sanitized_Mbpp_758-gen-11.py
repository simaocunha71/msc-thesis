from collections import Counter
def unique_sublists(lst):
  return {tuple(l): count for l, count in Counter(tuple(x) for x in lst).items()}