
from collections import Counter
def max_occurrences(my_list):
  c = Counter(my_list)
  return c.most_common(1)[0][0]


