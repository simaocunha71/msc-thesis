
import operator
def expensive_items(items, n):
  return sorted(items, key = operator.itemgetter('price'), reverse = True)[:n]


