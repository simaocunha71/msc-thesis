def expensive_items(dataset: list,n: int) -> list:
  expensive_items = sorted(dataset, key=lambda x: x['price'], reverse=True)[:n]
  return expensive_items


