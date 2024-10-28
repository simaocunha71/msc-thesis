def expensive_items(data: list, n: int) -> list:
  data.sort(key=lambda x: x['price'], reverse=True)
  return data[:n]  # Return the n most expensive items