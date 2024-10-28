
from collections import Counter
def sort_counter(d: dict) -> list:
  return sorted(d.items(), key=lambda item: item[1], reverse=True)


