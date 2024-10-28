
from collections import Counter
def max_occurrences(nums):
  counts = Counter(nums)
  return max(counts, key=counts.get)


