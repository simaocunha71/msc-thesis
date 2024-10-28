from collections import Counter
def max_occurrences(lst):
  counts = Counter(lst)
  max_count = max(counts.values())
  return [num for num, count in counts.items() if count == max_count]