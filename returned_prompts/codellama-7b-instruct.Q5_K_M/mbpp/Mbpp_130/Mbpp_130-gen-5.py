
from collections import Counter
def max_occurrences(mylist):
  return Counter(mylist).most_common(1)[0][0]


