def rotate_right(lst: list, n: int) -> list:
  return lst[-n:] + lst[:-n]

