from collections import Counter
def max_occurrences(lst: list) -> int:
  counter = Counter(lst)
  return counter.most_common(1)[0][0]