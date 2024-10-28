
def expensive_items(dataset: list,n: int) -> list:
  def key_function(item):
    return item['price']

  return sorted(dataset, key=key_function, reverse=True)[:n]


