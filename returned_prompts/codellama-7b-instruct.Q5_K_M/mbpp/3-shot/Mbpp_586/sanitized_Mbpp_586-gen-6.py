def split_Arr(Arr: list,n: int) -> list:
  Arr.insert(n, Arr.pop(0))
  return Arr