from collections import Counter
def max_occurrences(lst):
  counter = Counter(lst)
  return max(counter, key=counter.get)