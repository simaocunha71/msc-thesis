from collections import Counter
def max_occurrences(lst):
  freq = Counter(lst)
  return max(freq, key=freq.get)  # returns the item with the maximum frequency