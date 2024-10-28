def expensive_items(dataset: list,n: int) -> list:
  dataset.sort(key=lambda x: x['price'],reverse=True)
  return dataset[:n]