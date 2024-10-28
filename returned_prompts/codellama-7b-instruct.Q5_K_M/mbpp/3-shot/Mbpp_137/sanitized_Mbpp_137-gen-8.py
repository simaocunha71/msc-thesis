from collections import Counter
from math import log
def zero_count(nums):
  count = Counter(nums)
  total = len(nums)
  zeroes = count[0]
  non_zeroes = total - zeroes
  return zeroes / non_zeroes