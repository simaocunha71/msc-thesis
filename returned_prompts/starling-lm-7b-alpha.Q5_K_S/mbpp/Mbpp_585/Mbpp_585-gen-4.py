
def expensive_items(items: list, n: int) -> list:
  sorted_items = sorted(items, key=lambda item: item['price'], reverse=True)
  return sorted_items[:n]


