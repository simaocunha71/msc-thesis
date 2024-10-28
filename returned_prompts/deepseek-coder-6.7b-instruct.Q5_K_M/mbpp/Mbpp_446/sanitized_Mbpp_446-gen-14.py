def count_Occurrence(tup: tuple,lst: list) -> int:
  return sum(tup.count(i) for i in lst)