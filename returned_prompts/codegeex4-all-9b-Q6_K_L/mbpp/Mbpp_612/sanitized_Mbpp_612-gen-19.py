def merge(lists: list) -> list:
  result = list(zip(*lists))
  return result