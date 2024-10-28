
def expensive_items(dataset: list, n: int) -> list:
  sorted_dataset = sorted(dataset, key=lambda x: x['price'], reverse=True)
  return sorted_dataset[:n]


