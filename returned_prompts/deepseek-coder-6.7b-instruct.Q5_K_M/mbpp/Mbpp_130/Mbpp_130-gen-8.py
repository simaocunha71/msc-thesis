
from collections import Counter
def max_occurrences(lst):
  count = Counter(lst)
  return count.most_common(1)[0][0]


