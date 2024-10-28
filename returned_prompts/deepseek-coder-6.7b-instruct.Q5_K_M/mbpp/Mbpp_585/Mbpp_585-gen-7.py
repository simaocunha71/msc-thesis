
import operator
def expensive_items(items: list,n: int) -> list:
  sorted_items = sorted(items, key=operator.itemgetter('price'), reverse=True)
  return sorted_items[:n]


