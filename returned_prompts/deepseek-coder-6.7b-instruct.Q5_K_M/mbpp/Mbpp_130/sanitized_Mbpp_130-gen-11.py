from collections import Counter
def max_occurrences(lst):
  count = Counter(lst)
  return max(count, key=count.get)