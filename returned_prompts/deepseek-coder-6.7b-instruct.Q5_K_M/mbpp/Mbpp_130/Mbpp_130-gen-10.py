
from collections import Counter
def max_occurrences(nums):
  counter = Counter(nums)
  return counter.most_common(1)[0][0]


