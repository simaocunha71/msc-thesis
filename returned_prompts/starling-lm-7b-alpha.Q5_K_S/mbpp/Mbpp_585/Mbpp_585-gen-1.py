
def expensive_items(items: list,n: int) -> list:
  sorted_items = sorted(items, key=lambda x: x['price'],reverse=True)
  return sorted_items[:n]


