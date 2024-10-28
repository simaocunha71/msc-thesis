def list_split(lst: list,n: int) -> list:
  return [lst[i::n] for i in range(n)]