
from collections import Counter
def max_occurrences(my_list):
  return Counter(my_list).most_common(1)[0][0]


