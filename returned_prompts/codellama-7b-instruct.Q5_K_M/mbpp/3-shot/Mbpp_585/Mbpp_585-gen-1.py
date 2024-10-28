
def expensive_items(dataset: list, n: int) -> list:
  return sorted(dataset, key=lambda x: x['price'], reverse=True)[:n]


