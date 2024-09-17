
def expensive_items(items,n):
  sorted_items = sorted(items,key = lambda x: x['price'],reverse = True)
  return sorted_items[:n]


