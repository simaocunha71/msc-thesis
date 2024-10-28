def expensive_items(items: list, n: int) -> list:
  expensive_items = sorted(items, key=lambda x: x['price'], reverse=True)[:n]
  return expensive_items