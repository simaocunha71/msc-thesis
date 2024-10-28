
from collections import Counter
def max_occurrences(my_list: list) -> int:
  counter = Counter(my_list)
  max_count = max(counter.values())
  max_item = [k for k, v in counter.items() if v == max_count]
  return max_item[0]


