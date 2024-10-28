
from collections import Counter
def max_occurrences(nums):
  return Counter(nums).most_common(1)[0][0]


