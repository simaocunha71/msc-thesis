
import operator
def expensive_items(items: list,n: int) -> list:
  return sorted(items, key = operator.itemgetter('price'), reverse = True)[:n]


