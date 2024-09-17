def is_samepatterns(lst1: list, lst2: list) -> bool:
  return len(set(zip(lst1, lst2))) == len(lst1) == len(lst2)