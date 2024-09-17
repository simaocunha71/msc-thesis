def expensive_items(data: list,n: int) -> list:
  return sorted(data,key=lambda x: x['price'],reverse=True)[:n]