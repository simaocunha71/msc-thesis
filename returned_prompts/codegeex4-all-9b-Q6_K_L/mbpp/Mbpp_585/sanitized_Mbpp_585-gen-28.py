def expensive_items(items: list, n: int) -> list:
  return sorted(items, key=lambda x: x['price'], reverse=True)[:n]