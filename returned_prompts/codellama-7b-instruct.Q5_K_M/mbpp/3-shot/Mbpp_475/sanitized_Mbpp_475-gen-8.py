from collections import Counter
def sort_counter(counter: dict) -> list:
  return sorted(counter.items(), key=lambda item: item[1], reverse=True)