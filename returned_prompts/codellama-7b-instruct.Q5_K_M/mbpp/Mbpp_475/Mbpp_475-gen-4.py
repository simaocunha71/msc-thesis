
from collections import Counter

def sort_counter(counter: dict) -> list:
  sorted_dict = sorted(counter.items(), key=lambda item: item[1], reverse=True)
  return sorted_dict


