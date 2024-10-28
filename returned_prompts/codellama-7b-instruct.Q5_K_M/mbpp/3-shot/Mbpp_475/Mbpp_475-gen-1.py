
from collections import Counter
def sort_counter(counter: dict) -> list:
  sorted_counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)
  return sorted_counter


