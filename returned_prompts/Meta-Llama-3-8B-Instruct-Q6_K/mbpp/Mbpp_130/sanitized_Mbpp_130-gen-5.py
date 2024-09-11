from collections import Counter
def max_occurrences(lst):
  frequency = Counter(lst)
  return max(frequency, key=frequency.get)