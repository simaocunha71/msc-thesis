def get_median(lst1: list, lst2: list, size: int) -> float:
  lst = lst1 + lst2
  lst.sort()
  return lst[size-1]