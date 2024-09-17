from collections import Counter
def sort_counter(count: dict) -> list:
  sorted_counter = sorted(count.items(), key=lambda item: item[1], reverse=True)
  return sorted_counter