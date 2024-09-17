import heapq
def expensive_items(data: list,n: int) -> list:
  expensive_items = heapq.nlargest(n, data, key=lambda x: x['price'])
  return expensive_items