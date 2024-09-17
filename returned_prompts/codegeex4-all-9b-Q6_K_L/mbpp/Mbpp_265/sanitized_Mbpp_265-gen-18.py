def list_split(lst: list, n: int) -> list:
  return [lst[i:i+n] for i in range(0, len(lst), n)]