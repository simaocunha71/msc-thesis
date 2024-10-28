
from collections import Counter
def frequency_lists(lists):
  return dict(Counter(sum(lists, [])))


