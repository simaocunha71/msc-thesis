from collections import Counter
def unique_sublists(lst: list) -> dict:
  return {tuple(l): count for l, count in Counter(tuple(sublist) for sublist in lst).items()}