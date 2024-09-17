def last(array: list, elem: int) -> int:
  return len(array) - 1 - array[::-1].index(elem)

