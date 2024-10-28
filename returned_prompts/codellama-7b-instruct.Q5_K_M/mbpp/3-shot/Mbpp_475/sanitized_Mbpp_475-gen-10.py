from collections import Counter
def sort_counter(count: Counter) -> list:
  sorted_count = sorted(count.items(), key=lambda item: item[1], reverse=True)
  return sorted_count