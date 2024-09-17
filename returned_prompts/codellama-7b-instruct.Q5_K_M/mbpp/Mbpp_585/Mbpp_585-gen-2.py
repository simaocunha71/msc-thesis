
def expensive_items(dataset: list,n: int) -> list:
  expensive_items = sorted(dataset, key=lambda k: k['price'], reverse=True)[:n]
  return expensive_items


