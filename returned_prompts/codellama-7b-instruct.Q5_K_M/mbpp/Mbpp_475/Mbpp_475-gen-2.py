
from collections import Counter
def sort_counter(c: Counter) -> list:
  return sorted(c.items(), key=lambda item: item[1], reverse=True)


